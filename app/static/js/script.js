$(document).ready(function(){
  $(a#comm).on("click", function(){
    $.post("about.html"), function(data){
        $("#myModalDiv").html(data).fadeIn();
    });
  });
});
function vote(status) {
  function vote_data(status){
    var currentVote = document.getElementById(status).firstChild.data;
    parseInt(currentVote) + 1
    return parseInt(currentVote) + 1
  };
document.getElementById(status).innerHTML = vote_data(status);
};
