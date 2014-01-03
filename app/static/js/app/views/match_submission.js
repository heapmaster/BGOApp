console.log("Loading views/match_submission.js");

App.Views.MatchSubmissionView = Backbone.View.extend({
  templateName: 'match_submission.html',
  initialize: function(options){
    _.bindAll(this, 'render', 'update_game', 'update_duration', 'select_country', 'select_position', 'add_standing', 'delete_standing', 'submit_match');
    
    var currentView = this;
    
/*     this.model.on('scoreboard_load_succeed', this.render); */

    this.model = new App.Models.Match();
        
    this.gameCollection = new App.Collections.GameCollection();
    this.countryCollection = new App.Collections.CountryCollection();
    
    this.submission_result = options.submission_result;
    
    $.when(this.gameCollection.fetch(), this.countryCollection.fetch()).done(function() {
      currentView.selectedGame = currentView.gameCollection.models[0];
      currentView.selectedDuration = 1;  
      $.when(currentView.render()).done(function() {
        currentView.render();
      });
    });
  },
  
  render: function(){
    var data = {
      games: new Array(),
      standings: new Array(),
      countries: new Array(),
      selectedGame: this.selectedGame,
      selectedDuration: this.selectedDuration,
      submission_result: this.submission_result
/*
      positions: _.range(1, this.selectedGame.attributes.max_players + 1),
      coop: this.selectedGame.attributes.coop
*/
    };

    _.each(this.gameCollection.models, function(game) {
      data.games.push(game);
    });

    _.each(this.countryCollection.models, function(country) {
      data.countries.push(country);
    });

    _.each(_.sortBy(this.model.attributes.players, function(standing) { return standing.place; }), function(standing) {
      data.standings.push({ 'country': _.find(data.countries, function(country) { return country.attributes.id == standing.player_id}), 'position': standing.place });
    });
    
    var compiledTemplate = _.template(this.template, data);
    
    this.$el.html(compiledTemplate);
    
    return this;
  },
  
  events: {
    'change #inputGameName'      : 'update_game',
    'change #inputGameDuration'  : 'update_duration',
    'click #submit-pair'         : 'add_standing',
    'click .teams a'             : 'select_country',
    'click .positions a'         : 'select_position',
    'click .delete-pair'         : 'delete_standing',
    'click #submit-match'        : 'submit_match'
  },
  
  update_game: function(event) {
    this.selectedGame = _.find(this.gameCollection.models, function(game) { return game.attributes.id == $('#inputGameName').val()});
    this.render();
  },
  
  update_duration: function(event) {
    this.selectedDuration = $('#inputGameDuration').val();
    this.render();
  },
  
  select_country: function(event) {
    $(event.currentTarget).addClass('active').siblings().removeClass('active');
    this.selectedCountry = event.currentTarget.getAttribute('country_id');
  },
  
  select_position: function(event) {
    $(event.currentTarget).addClass('active').siblings().removeClass('active');
    this.selectedPosition = event.currentTarget.getAttribute('position_id');
  },
  
  add_standing: function(event) {
    console.log('selected country: ', this.selectedCountry);
    console.log('selected position: ', this.selectedPosition);

    this.model.attributes.players.push({ 'player_id': this.selectedCountry, 'place': this.selectedPosition });

    $('#myModal').modal('hide');
    $('body').removeClass('modal-open');
    $('.modal-backdrop').remove();    

    this.render();
  },
  delete_standing: function(event) {
    var del_id = $(event.currentTarget).parent().siblings('.country-cell').attr('country_id');
    var del_obj = _.find(this.model.attributes.players, function(standing) { return standing.player_id == del_id});
    
    this.model.attributes.players = _.reject(this.model.attributes.players, function(standing) { return standing == del_obj; });
    
    this.render();
  },
  submit_match: function(event) {    
    this.model.attributes.game_id = $('#inputGameName').val();
    this.model.attributes.duration_id = $('#inputGameDuration').val();
    
    console.log(this.model);
    this.model.save();
    
    window.location.reload();
    
/*
    this.model = new App.Models.Match();

    this.selectedGame = this.gameCollection.models[0];
    this.selectedDuration = 1;
    $("#standings-list").html('');

    $('.alert').show();
    $("html, body").animate({ scrollTop: 0 }, "slow");
*/
  }
});