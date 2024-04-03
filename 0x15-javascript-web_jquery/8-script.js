$(function () {
	    $("DIV#red_header").click(function () {
		      $(function () {
			          $.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
					        let movie = data.results;
					        for (let movie in movie) {
							        $("UL#list_movies").append("<li>" + films[film].title + "</li>");
							      }
					      });
			        });
