console.log("Loading models/match.js");

App.Models.Match = Backbone.Model.extend({
  url: 'http://bgo.herokuapp.com/matches',
  defaults: {
    game_id: '',
    duration_id: '',
    players: []
  }
});
