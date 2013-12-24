console.log("Loading models/game.js");

App.Models.GameDetail = Backbone.Model.extend({
  defaults: {
    id: '', 
    name: '', 
    category: '', 
    numPlayers: '', 
    playingTime: '', 
    difficulty: '', 
    points: '',
    description: '', 
    icon: ''
  },
  initialize: function(options){
    _.bindAll(this, 'success_handler', 'fetch_data');
    
    Backbone.Mediator.subscribeOnce('game_list_load_succeed', this.fetch_data);
    
    this.url = 'http://fast-caverns-5319.herokuapp.com/game/' + options.game_id + '/';
  },
  fetch_data: function() {
    this.fetch({success: this.success_handler});
    console.log("trigger received");
  },
  success_handler: function() {
    console.log("fired next trigger");
    this.trigger("game_detail_load_succeed");
  },
});
