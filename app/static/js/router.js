console.log("Loading router.js");

App.AppRouter = Backbone.Router.extend({
  routes: {
/*         ''                          : 'showLanding', */
    'games/:game_id'            : 'showGameDetail',
/*
        'search/:query'             : 'showSearch',
        'library/:library_id'       : 'showLibrary',
        'pooled_set/:ps_id'         : 'showPooledSet',
        'flowcell/:flowcell_id'     : 'showFlowcell',
        'barcoded_library/:bclib_id': 'showBarcodedLibrary',
        'general-status'            : 'showStatus',
        'browse'                    : 'showBrowse',
        'suggestions'               : 'showSuggestions',
        'dataset'                   : 'showDataset'
*/
  },
  showGameDetail: function(game_id) {
    if (!($("#detail").length > 0)) {
      var gameListView = new App.Views.GameListView({ el: $("#main") });
    }
    var gameDetailView = new App.Views.GameDetailView({ el: $("#detail"), dom_name: "#detail", game_id: game_id });
    console.log(game_id);
  },
/*
    showLanding: function(query) {
        var landingView = new App.Views.LandingView({ el: $("#main") });
        window.scrollTo(0, 0);
    },
    showSearch: function(query) {
        var searchView = new App.Views.SearchResultsView({ el: $("#main"), query: query });
        window.scrollTo(0, 0);
    },
    showLibrary: function(library_id) {
        var libView = new App.Views.LibraryDetailView({ el: $("#main"), library_id: library_id });
        window.scrollTo(0, 0);
    },
    showPooledSet: function(ps_id) {
        var pooledSetView = new App.Views.PooledSetDetailView({ el: $("#main"), ps_id: ps_id });
        window.scrollTo(0, 0);
    },
    showFlowcell: function(flowcell_id) {
        var flowView = new App.Views.FlowcellDetailView({ el: $("#main"), flowcell_id: flowcell_id });
        window.scrollTo(0, 0);
    },
    showBarcodedLibrary: function(bclib_id) {
        var bclibView = new App.Views.BarcodedLibraryDetailView({ el: $("#main"), bclib_id: bclib_id });
        window.scrollTo(0, 0);
    },
    showStatus: function() {
        var statusView = new App.Views.FlowcellStatusView({ el: $("#main") });
        window.scrollTo(0, 0);
    },
    showSuggestions: function() {
        var suggestionView = new App.Views.SuggestionView({ el: $("#main") });
        window.scrollTo(0,0);
    },
    showDataset: function() {
        var datasetView = new App.Views.DatasetView({ el: $("#main") });
        window.scrollTo(0,0);
    }
*/
});
