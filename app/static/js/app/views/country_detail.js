console.log("Loading views/country_detail.js");

App.Views.CountryDetailView = Backbone.View.extend({
  templateName: 'country_detail.html',
  initialize: function(options){
    _.bindAll(this, 'render', 'report');
    this.dom_name = options.dom_name;
    
    this.model = new App.Models.CountryDetail({ game_id: options.game_id });

    this.model.on('country_detail_load_succeed', this.report);
  },
  render: function(){
    var compiledTemplate = _.template(this.template, this.model.attributes);

    $(this.dom_name).html(compiledTemplate);
    
    return this;
  },
  report: function(){
    this.render();
  }
});
