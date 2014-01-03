console.log("Loading views/rules.js");

App.Views.RulesView = Backbone.View.extend({
  templateName: 'rules.html',
  initialize: function(options){
    _.bindAll(this, 'render');
    
    this.render();
  },
  
  render: function(){    
    this.$el.html(this.template);
    
    return this;
  }
});