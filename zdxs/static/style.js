
    $(document).ready(function(){
      $("#passages img").addClass("img-responsive");

      $(".hovernav").mouseenter (function(){
        $(this).css({"background":"#B46969","color":"red"});
      });
      $(".hovernav").mouseleave (function(){
        $(this).css("background","#222")

      });
      $(".col-list").mouseenter(function(){
      	$(this).css("box-shadow","0 0 5px 5px #E1E0E0");
      })
      $(".col-list").mouseleave(function(){
      	$(this).css("box-shadow","0 0 5px 5px #EEE");
      });
      $(".data_post").mouseenter(function(){
        $(this).css("box-shadow","0 0 5px 5px #D2CECE");
      });
      $(".data_post").mouseleave(function(){
        $(this).css("box-shadow","0 0 5px 5px #E7E4E4");
      })
    });

