console.log("Loading views/country_list.js");

App.Views.CountryListView = Backbone.View.extend({
  templateName: 'country_list.html',
  initialize: function(options){
    _.bindAll(this, 'render');
    
    this.model = new App.Models.CountryList();
    
    this.model.on('load_succeed', this.render);
  },
  render: function(){    
    var data = {
      countryList: new Array(),
      _: _
    };
    
    _.each(this.model.attributes.games, function(game) {
      data.countryList.push(game);
    });

    var compiledTemplate = _.template(this.template, data);
    
    this.$el.html(compiledTemplate);
    
    Backbone.Mediator.pub('country_list_load_succeed');
    
    return this;
  }
});