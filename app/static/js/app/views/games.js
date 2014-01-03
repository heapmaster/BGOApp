console.log("Loading views/games.js");

App.Views.GamesView = Backbone.View.extend({
  templateName: 'games_master_detail.html',
  initialize: function(options){
    _.bindAll(this, 'render', 'select_game');
    
    var currentView = this;
    
    this.gameCollection = new App.Collections.GameCollection;
    this.matchCollection = new App.Collections.MatchCollection;
    
    this.selectedGameID = options.game_id;
    
    $.when(this.gameCollection.fetch(), this.matchCollection.fetch()).done(function() {
      $.when(currentView.render()).done(function() {
        currentView.render();
      });
    });
  },
  
  render: function(){    
    var game_id = this.selectedGameID;

    var data = {
      gameList: new Array(),
      gameCollection: '',
      game_log: '',
      selectedGame: '',
      imgCellHeight: $("#img-cell").width(),
      _: _
    };
    
    _.each(this.gameCollection.models, function(game) {
      data.gameList.push(game);
    });
    
    data.gameCollection = this.gameCollection;
    
    if (game_id != 0) {
      data.selectedGame = _.find(this.gameCollection.models, function(game) { return game.attributes.id == game_id; });
      data.game_log = this.matchCollection.get_matches_by_game(data.selectedGame.attributes.id);
      console.log(data.game_log);
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