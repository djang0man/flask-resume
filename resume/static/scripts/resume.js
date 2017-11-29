'use strict';

function Resume(resumeDataObj) {
  this.resume = resumeDataObj;
}

Resume.local = [];

Resume.prototype.toHtml = function() {
  let template = Handlebars.compile($('#resume-template').html());
  return template(this.resume);
};

Resume.load = function(resumeData) {
  Resume.local.push(new Resume(resumeData));
}

Resume.setLocalStorage = function(path) {
  $.getJSON(path).then(function(data) {
    localStorage.rawResume = JSON.stringify(data);
    Resume.load(JSON.parse(localStorage.rawResume));
    resumeView.initPage();
  },
  function(error) {
    console.log(error);
  });
}

Resume.fetch = function() {
  if (localStorage.rawResume) {
    $.ajax({
      url: '/api/stuartdkershaw',
      method: 'HEAD'
    })
    .done(function(data, message, xhr) {
      var eTag = xhr.getResponseHeader('eTag');
      if (eTag === localStorage.eTag) {
        Resume.load(JSON.parse(localStorage.rawResume));
        resumeView.initPage();
      } else {
        Resume.setLocalStorage('/api/stuartdkershaw');
      }
    })
    .fail(function(error) {
      console.log(error);
    });
  } else {
    $.ajax({
      url: '/api/stuartdkershaw',
      method: 'HEAD'
    })
    .done(function(data, message, xhr) {
      localStorage.eTag = xhr.getResponseHeader('eTag');
    })
    .fail(function(error) {
      console.log(error);
    });
    Resume.setLocalStorage('/api/stuartdkershaw');
  }
}
