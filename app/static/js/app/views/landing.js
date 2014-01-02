console.log("Loading views/landing.js");

App.Views.LandingView = Backbone.View.extend({
  templateName: 'landing.html',
  initialize: function(options){
    _.bindAll(this, 'render');
    
    this.render();
  },
  
  render: function(){    
    this.$el.html(this.template);
    
    return this;
  }
});