console.log("Loading views/countries.js");

App.Views.CountriesView = Backbone.View.extend({
  templateName: 'countries_master_detail.html',
  initialize: function(options){
    _.bindAll(this, 'render', 'select_country');
    
    var currentView = this;
    
    this.countryCollection = new App.Collections.CountryCollection;
    this.standingCollection = new App.Collections.StandingCollection;
    
    this.selectedCountryID = options.country_id;
    
    $.when(this.countryCollection.fetch(), this.standingCollection.fetch()).done(function() {
      $.when(currentView.render()).done(function() {
        currentView.render();
      });
    });
  },
  
  render: function(){    
    var country_id = this.selectedCountryID;

    var data = {
      countryList: new Array(),
      selectedCountry: '',
      ranking: '',
      percentage: '',
      score: '',
      imgCellHeight: $("#img-cell").width(),
      _: _
    };
    
    _.each(this.countryCollection.models, function(country) {
      data.countryList.push(country);
    });
    
    if (country_id != 0) {
      data.selectedCountry = _.find(this.countryCollection.models, function(country) { return country.attributes.id == country_id; });
      data.ranking = this.standingCollection.get_ranking(data.selectedCountry.attributes.id);
      data.percentage = this.standingCollection.get_percentage(data.selectedCountry.attributes.id);
      data.score = data.selectedCountry.attributes.points;
    }    
    
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