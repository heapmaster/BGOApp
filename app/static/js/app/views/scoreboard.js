console.log("Loading views/scoreboard.js");

App.Views.ScoreboardView = Backbone.View.extend({
  templateName: 'scoreboard.html',
  initialize: function(options){
    _.bindAll(this, 'render');
    
    this.model = new App.Models.Scoreboard();
    
    this.model.on('scoreboard_load_succeed', this.render);
  },
  render: function(){    
    var data = {
      countries: new Array(),
      max_score: 0,
      _: _
    };
    
    _.each(_.sortBy(this.model.attributes.scores, function(country){ return country.score * -1; }), function(country) {
      data.countries.push(country);
    });
    
    data.max_score = data.countries[0].score;

    var compiledTemplate = _.template(this.template, data);
    
    this.$el.html(compiledTemplate);
    
    return this;
  }
});