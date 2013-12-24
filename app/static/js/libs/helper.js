console.log('Loading js/libs/helper.js');

var App = {};
App.Views = {};
App.Models = {};
App.Collections = {};

$(document).ready(function(){
});

App.TemplateManager = {
    prefix: "static/templates/",
    loadTemplates: function(views, callback) {
        var reduced_views = _.filter(views, function(view) { return _.has(view.prototype, "templateName") });
        var loadTemplate = function(index, ctx) {
            var view = reduced_views[index];
            var name = view.prototype.templateName;
            console.log('Loading template: ' + name);
            $.get(ctx.prefix + name, function(data) {
                view.prototype.template = data;
                index++;
                if (index < reduced_views.length) {
                    loadTemplate(index, ctx);
                } else {
                    callback();
                }
            });
        }
        loadTemplate(0, this);
    },
};
