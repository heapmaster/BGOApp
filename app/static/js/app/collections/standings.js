console.log("Loading collections/standings.js");

App.Collections.StandingCollection = Backbone.Collection.extend({
  model: App.Models.Standing,
  url: 'http://bgo.herokuapp.com/scores',
  parse: function(response) {
    return response.scores;
  }
});
