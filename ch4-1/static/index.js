
    $(document).ready(function () {
      showArticles();
    });

    function openClose() {
      // id 값 post-box의 display 값이 block 이면(= 눈에 보이면)
      if ($("#post-box").css("display") == "block") {
        // post-box를 가리고
        $("#post-box").hide();
        // 다시 버튼을 클릭하면, 박스 열기를 할 수 있게 텍스트 바꿔두기
        $("#btn-post-box").text("포스팅 박스 열기");
      } else {
        // 아니면(눈에 보이지 않으면) post-box를 펴라
        $("#post-box").show();
        // 다시 버튼을 클릭하면, 박스 닫기를 할 수 있게 텍스트 바꿔두기
        $("#btn-post-box").text("포스팅 박스 닫기");
      }
    }
    function postArticle() {

      // 2. memo에 POST 방식으로 메모 생성 요청하기
      $.ajax({
        type: "POST", // POST 방식으로 요청하겠다.
        url: "/memo", // /memo라는 url에 요청하겠다.
        data: {
          url_give: $("#post-url").val(),
          comment_give: $("#post-comment").val()
        }, // 데이터를 주는 방법
        success: function (response) { // 성공하면
          if (response["result"] == "success") {
            alert("포스팅 성공!");
            // 3. 성공 시 리스트 새로고침하기
            showArticles();
          } else {
            alert("서버 오류!")
          }
        }
      })
    }
    function showArticles() {
      $("#cards-box").html("");
      $.ajax({
        type: "GET",
        url: "/memo",
        data: {},
        success: function (response) {
          let articles = response["articles"];
          // console.log(articles);
          for (let i = 0; i < articles.length; i++) {
            makeCard(
              articles[i]["image"], 
              articles[i]["url"], 
              articles[i]["title"], 
              articles[i]["desc"],
              articles[i]["comment"]
            );
          }
        }
      });
    }
    function makeCard(image, url, title, desc, comment) {
      let tempHtml = `<div class="card">
                        <img class="card-img-top" src="${image}" alt="Card image cap">
                        <div class="card-body">
                        <a href="${url}" target="_blank" class="card-title">${title}</a>
                        <p class="card-text">${desc}</p>
                        <p class="card-text comment">${comment}</p>
                        </div>
                    </div>`;
      $("#cards-box").append(tempHtml);
    }