console.log("Loading views/matches.js");

App.Views.MatchesView = Backbone.View.extend({
  templateName: 'matches.html',
  initialize: function(options){
    _.bindAll(this, 'render');
    
    var currentView = this;

    this.matchCollection = new App.Collections.MatchCollection;
    this.gameCollection = new App.Collections.GameCollection;
    
    $.when(this.matchCollection.fetch(), this.gameCollection.fetch()).done(function() {
      currentView.render();
    });
    
    this.render();
  },
  
  render: function(){
    var data = {
      matches: '',
      games: '',
      _: _
    };
    
    data.matches = this.matchCollection.get_matches();
    data.games = this.gameCollection;
    
    var compiledTemplate = _.template(this.template, data);
    
    this.$el.html(compiledTemplate);
    
    return this;
  }
});