console.log("Loading views/scoreboard.js");

App.Views.ScoreboardView = Backbone.View.extend({
  templateName: 'scoreboard.html',
  initialize: function(options){
    _.bindAll(this, 'render', 'select_country');
    
    var currentView = this;
    
    this.standingCollection = new App.Collections.StandingCollection;
    
    $.when(this.standingCollection.fetch()).done(function() {
      currentView.render();
    });    
  },
  
  render: function(){    
    var data = {
      countries: new Array(),
      max_score: 0,
      _: _
    };
    
    _.each(_.sortBy(this.standingCollection.models, function(country){ return country.attributes.score * -1; }), function(country) {
      data.countries.push(country);
    });
    
    data.max_score = data.countries[0].attributes.score;

    console.log(data.countries);
    console.log('max score', data.max_score);
    
    var compiledTemplate = _.template(this.template, data);
    
    this.$el.html(compiledTemplate);
    
    return this;
  },
  
  events: {
    'click .country-selector': 'select_country'
  },
  
  select_country: function(event) {
    window.location.href = '#countries/' + event.currentTarget.getAttribute('country_id');
  }
});