console.log("Loading views/game_detail.js");

App.Views.GameDetailView = Backbone.View.extend({
  templateName: 'game_detail.html',
  initialize: function(options){
    _.bindAll(this, 'render', 'report');
    this.dom_name = options.dom_name;
    
    this.model = new App.Models.GameDetail({ game_id: options.game_id });

    this.model.on('game_detail_load_succeed', this.report);
  },
  render: function(){
    var compiledTemplate = _.template(this.template, this.model.attributes);

    $(this.dom_name).html(compiledTemplate);
/*
    this.$el.html(compiledTemplate);
    console.log(this.$el.html());
*/
    
    return this;
  },
  report: function(){
    console.log("last trigger received");
    this.render();
  }
});
