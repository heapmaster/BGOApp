console.log("Loading app.js");
  
App.TemplateManager.loadTemplates(_.values(App.Views), function() {
    App.Router = new App.AppRouter();
    App.Router.initialize();
    Backbone.history.start();
});
