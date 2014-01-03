console.log("Loading collections/games.js");

App.Collections.GameCollection = Backbone.Collection.extend({
  model: App.Models.Game,
  url: 'http://bgo.herokuapp.com/games',
  initialize: function(options) {
    _.bindAll(this, 'get_name_by_id', 'get_img_by_id');
  },
  parse: function(response) {
    return response.games;
  },
  get_name_by_id: function(game_id) {
    var selected_game = _.find(this.models, function(game) { return game.attributes.id == game_id; });
    
    return selected_game.attributes.name;
  },
  get_img_by_id: function(game_id) {
    var selected_game = _.find(this.models, function(game) { return game.attributes.id == game_id; });
    
    return selected_game.attributes.icon;
  }
});
