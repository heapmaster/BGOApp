console.log("Loading router.js");

App.AppRouter = Backbone.Router.extend({
  routes: {
    ''                                          : 'showLanding',
    'games'                                     : 'showGames',
    'games/:game_id'                            : 'showGameDetail',
    'countries'                                 : 'showCountries',
    'countries/:country_id'                     : 'showCountryDetail',
    'scoreboard'                                : 'showScoreboard',
    'rules'                                     : 'showRules',
    'matches'                                   : 'showMatches',
    'match_submission'                          : 'showMatchSubmission',
    'match_submission/:submission_result'       : 'showMatchSubmissionResult'
  },
  showLanding: function() {
    var landingView = new App.Views.LandingView({ el: $("#main") });
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showGames: function() {
    var gamesView = new App.Views.GamesView({ el: $("#main"), game_id: 0 });
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showGameDetail: function(game_id) {
    var gamesView = new App.Views.GamesView({ el: $("#main"), game_id: game_id });
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showCountries: function() {
    var countriesView = new App.Views.CountriesView({ el: $("#main"), country_id: 0 });
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showCountryDetail: function(country_id) {
    var countriesView = new App.Views.CountriesView({ el: $("#main"), country_id: country_id });
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showScoreboard: function() {
    var scoreboardView = new App.Views.ScoreboardView({ el: $("#main") });
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showRules: function() {
    var rulesView = new App.Views.RulesView({ el: $("#main") });
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showMatches: function() {
    var rulesView = new App.Views.MatchesView({ el: $("#main") });
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showMatchSubmission: function() {
    var matchSubmissionView = new App.Views.MatchSubmissionView({ el: $("#main"), submission_result: 0 });
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showMatchSubmissionResult: function(submission_result) {
    var matchSubmissionView = new App.Views.MatchSubmissionView({ el: $("#main"), submission_result: submission_result });
    $("html, body").animate({ scrollTop: 0 }, "slow");
  }
});
