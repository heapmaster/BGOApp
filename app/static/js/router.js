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
    'match_submission'                          : 'showMatchSubmission'
 //   'match_submission/:submission_result'       : 'showMatchSubmissionResult'
  },
  showLanding: function() {
    if(!this.landingView) {
      this.landingView = new App.Views.LandingView({ el: $("#main") });
    }
    this.landingView.render();
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showGames: function() {
    if(!this.gamesView) {
      this.gamesView = new App.Views.GamesView({ el: $("#main"), game_id: 0 });
    }
    this.gamesView.render();
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showGameDetail: function(game_id) {
    new App.Views.GamesView({ el: $("#main"), game_id: game_id });
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showCountries: function() {
    if(!this.countriesView) {
      this.countriesView = new App.Views.CountriesView({ el: $("#main"), country_id: 0 });
    }
    this.countriesView.render();
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showCountryDetail: function(country_id) {
    new App.Views.CountriesView({ el: $("#main"), country_id: country_id });
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showScoreboard: function() {
    this.scoreboardView = new App.Views.ScoreboardView({ el: $("#main") });
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showRules: function() {
    if(!this.rulesView) {
      this.rulesView = new App.Views.RulesView({ el: $("#main") });
    }
    this.rulesView.render();
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showMatches: function() {
    this.MatchesView = new App.Views.MatchesView({ el: $("#main") });
    this.MatchesView.render();
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
  showMatchSubmission: function() {
    if(!this.matchSubmissionView) {
      this.matchSubmissionView = new App.Views.MatchSubmissionView({ el: $("#main"), submission_result: 0 });
    }
    this.matchSubmissionView.render();
    $("html, body").animate({ scrollTop: 0 }, "slow");
  },
 // showMatchSubmissionResult: function(submission_result) {
 //   new App.Views.MatchSubmissionView({ el: $("#main"), submission_result: submission_result });
 //   $("html, body").animate({ scrollTop: 0 }, "slow");
});
