console.log("Loading models/country_detail.js");

App.Models.CountryDetail = Backbone.Model.extend({
  initialize: function(options){
    _.bindAll(this, 'success_handler', 'fetch_data');
    
    Backbone.Mediator.subscribeOnce('country_list_load_succeed', this.fetch_data);
    
    this.url = 'http://bgo.herokuapp.com/country/' + options.country_id + '/';
  },
  fetch_data: function() {
    this.fetch({success: this.success_handler});
  },
  success_handler: function() {
    this.trigger("country_detail_load_succeed");
  },
});
