
console.log("Loading models/game.js");

App.Models.GameList = Backbone.Model.extend({
  defaults: {
  },
  initialize: function(options){
    _.bindAll(this, 'success_handler');
    
    this.url = 'http://bgo.herokuapp.com/games';
    this.fetch({success: this.success_handler});
  },
  success_handler: function() {
    this.trigger('load_succeed');
  }
});
