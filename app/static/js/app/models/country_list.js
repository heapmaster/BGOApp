console.log("Loading models/country_list.js");

App.Models.CountryList = Backbone.Model.extend({
  defaults: {
  },
  initialize: function(options){
    _.bindAll(this, 'success_handler');
    
    this.url = 'http://bgo.herokuapp.com/country';
    this.fetch({ success: this.success_handler });
  },
  success_handler: function() {
    this.trigger('load_succeed');
  }
});
