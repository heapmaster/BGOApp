console.log("Loading models/scoreboard.js");

App.Models.Scoreboard = Backbone.Model.extend({
  defaults: {
  },
  initialize: function(options){
    _.bindAll(this, 'success_handler');
    
    this.url = 'http://bgo.herokuapp.com/scores';
    this.fetch({success: this.success_handler});
  },
  success_handler: function() {
    this.trigger('scoreboard_load_succeed');
    console.log('scoreboard_load_succeed');
  }
});
