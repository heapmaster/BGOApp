console.log("Loading views/game_list.js");

App.Views.GameListView = Backbone.View.extend({
  templateName: 'game_list.html',
  initialize: function(options){
    _.bindAll(this, 'render');
    
    this.model = new App.Models.GameList();
    
    this.model.on('load_succeed', this.render);
  },
  render: function(){    
    this.$el.html(this.template);
    
    Backbone.Mediator.pub('game_list_load_succeed');
    
    return this;
  }
});
