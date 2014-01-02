console.log("Loading collections/games.js");

App.Collections.GameCollection = Backbone.Collection.extend({
  model: App.Models.Game,
  url: 'http://bgo.herokuapp.com/games',
  parse: function(response) {
    return response.games;
  }
});
