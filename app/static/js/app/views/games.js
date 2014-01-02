console.log("Loading views/games.js");

App.Views.GamesView = Backbone.View.extend({
  templateName: 'games_master_detail.html',
  initialize: function(options){
    _.bindAll(this, 'render', 'select_game');
    
    var currentView = this;
    
    this.gameCollection = new App.Collections.GameCollection;
    this.selectedGameID = options.game_id;
    
    $.when(this.gameCollection.fetch()).done(function() {
      $.when(currentView.render()).done(function() {
        currentView.render();
      });
    });
  },
  
  render: function(){    
    var game_id = this.selectedGameID;

    var data = {
      gameList: new Array(),
      selectedGame: '',
      imgCellHeight: $("#img-cell").width(),
      _: _
    };
    
    _.each(this.gameCollection.models, function(game) {
      data.gameList.push(game);
    });
    
    if (game_id != 0) {
      data.selectedGame = _.find(this.gameCollection.models, function(game) { return game.attributes.id == game_id; });
    }
    
    var compiledTemplate = _.template(this.template, data);
    
    this.$el.html(compiledTemplate);
    
    return this;
  },
  
  events: {
    'click .game-selector': 'select_game',
  },
  
  select_game: function(event) {
    window.location.href = '#games/' + event.currentTarget.getAttribute('game_id');
  }
});