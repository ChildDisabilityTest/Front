// place 6 cardnews components by random

$(document).ready(function () {
  // lightbox option
  lightbox.option({
    alwaysShowNavOnTouchDevices: true,
    positionFromTop: 180,
    wrapAround: true,
    disableScrolling: true,
  });

  // 1. 말이 느린 아이
  const card1 = `
        <a
            href="/static/img/cardnews/card1/1_1.png"
            data-lightbox="card1" data-title="말이 느린 아이"
        > <img src="/static/img/cardnews/card1/1_1.png" class="card-news-img"/>
        </a>
        <a
            href="/static/img/cardnews/card1/1_2.png"
            data-lightbox="card1" data-title="말이 느린 아이"
        ></a>
        <a
            href="/static/img/cardnews/card1/1_3.png"
            data-lightbox="card1" data-title="말이 느린 아이"
        ></a>
        <a
            href="/static/img/cardnews/card1/1_4.png"
            data-lightbox="card1" data-title="말이 느린 아이"
        ></a>
        <a
            href="/static/img/cardnews/card1/1_5.png"
            data-lightbox="card1" data-title="말이 느린 아이"
        ></a>
        <a
            href="/static/img/cardnews/card1/1_6.png"
            data-lightbox="card1" data-title="말이 느린 아이"
        ></a>
        <a
            href="/static/img/cardnews/card1/1_7.png"
            data-lightbox="card1" data-title="말이 느린 아이"
        ></a>
        <div class="card-news-title">말이 느린 아이</div>
  `;

  // 2. 스마트폰 사용
  const card2 = `
        <a
            href="/static/img/cardnews/card2/2_1.png"
            data-lightbox="card2" data-title="스마트폰 사용"
        > <img src="/static/img/cardnews/card2/2_1.png" class="card-news-img"/></a>
        <a
            href="/static/img/cardnews/card2/2_2.png"
            data-lightbox="card2" data-title="스마트폰 사용"
        ></a>
        <a
            href="/static/img/cardnews/card2/2_3.png"
            data-lightbox="card2" data-title="스마트폰 사용"
        ></a>
        <a
            href="/static/img/cardnews/card2/2_4.png"
            data-lightbox="card2" data-title="스마트폰 사용"
        ></a>
        <a
            href="/static/img/cardnews/card2/2_5.png"
            data-lightbox="card2" data-title="스마트폰 사용"
        ></a>
        <a
            href="/static/img/cardnews/card2/2_6.png"
            data-lightbox="card2" data-title="스마트폰 사용"
        ></a>
        <a
            href="/static/img/cardnews/card2/2_7.png"
            data-lightbox="card2" data-title="스마트폰 사용"
        ></a>
        <div class="card-news-title">스마트폰 사용</div>
  `;

  // 3. 홈티칭
  const card3 = `
    <a
        href="/static/img/cardnews/card3/3_1.png"
        data-lightbox="card3" data-title="홈티칭"
    > <img src="/static/img/cardnews/card3/3_1.png" class="card-news-img"/>
    </a>
    <a
        href="/static/img/cardnews/card3/3_2.png"
        data-lightbox="card3" data-title="홈티칭"
    ></a>
    <a
        href="/static/img/cardnews/card3/3_3.png"
        data-lightbox="card3" data-title="홈티칭"
    ></a>
    <a
        href="/static/img/cardnews/card3/3_4.png"
        data-lightbox="card3" data-title="홈티칭"
    ></a>
    <a
        href="/static/img/cardnews/card3/3_5.png"
        data-lightbox="card3" data-title="홈티칭"
    ></a>
    <a
        href="/static/img/cardnews/card3/3_6.png"
        data-lightbox="card3" data-title="홈티칭"
    ></a>
    <a
        href="/static/img/cardnews/card3/3_7.png"
        data-lightbox="card3" data-title="홈티칭"
    ></a>
    <a
        href="/static/img/cardnews/card3/3_8.png"
        data-lightbox="card3" data-title="홈티칭"
    ></a>
    <a
        href="/static/img/cardnews/card3/3_9.png"
        data-lightbox="card3" data-title="홈티칭"
    ></a>
    <div class="card-news-title">홈티칭</div>
  `;

  // 4. 느린 학습자
  const card4 = `
        <a
            href="/static/img/cardnews/card4/4_1.png"
            data-lightbox="card4" data-title="느린 학습자"
        > <img src="/static/img/cardnews/card4/4_1.png" class="card-news-img"/>
        </a>
        <a
            href="/static/img/cardnews/card4/4_2.png"
            data-lightbox="card4" data-title="느린 학습자"
        ></a>
        <a
            href="/static/img/cardnews/card4/4_3.png"
            data-lightbox="card4" data-title="느린 학습자"
        ></a>
        <a
            href="/static/img/cardnews/card4/4_4.png"
            data-lightbox="card4" data-title="느린 학습자"
        ></a>
        <a
            href="/static/img/cardnews/card4/4_5.png"
            data-lightbox="card4" data-title="느린 학습자"
        ></a>
        <a
            href="/static/img/cardnews/card4/4_6.png"
            data-lightbox="card4" data-title="느린 학습자"
        ></a>
        <a
            href="/static/img/cardnews/card4/4_7.png"
            data-lightbox="card4" data-title="느린 학습자"
        ></a>        
        <div class="card-news-title">느린 학습자</div>
  `;

  // 5. 떼쓰는 아이 대하는 자세
  const card5 = `
        <a
            href="/static/img/cardnews/card5/5_1.png"
            data-lightbox="card5" data-title="떼쓰는 아이 대하는 자세"
        > <img src="/static/img/cardnews/card5/5_1.png" class="card-news-img"/>
        </a>
        <a
            href="/static/img/cardnews/card5/5_2.png"
            data-lightbox="card5" data-title="떼쓰는 아이 대하는 자세"
        ></a>
        <a
            href="/static/img/cardnews/card5/5_3.png"
            data-lightbox="card5" data-title="떼쓰는 아이 대하는 자세"
        ></a>
        <a
            href="/static/img/cardnews/card5/5_4.png"
            data-lightbox="card5" data-title="떼쓰는 아이 대하는 자세"
        ></a>
        <a
            href="/static/img/cardnews/card5/5_5.png"
            data-lightbox="card5" data-title="떼쓰는 아이 대하는 자세"
        ></a>
        <a
            href="/static/img/cardnews/card5/5_6.png"
            data-lightbox="card5" data-title="떼쓰는 아이 대하는 자세"
        ></a>
        <a
            href="/static/img/cardnews/card5/5_7.png"
            data-lightbox="card5" data-title="떼쓰는 아이 대하는 자세"
        ></a>
        <a
            href="/static/img/cardnews/card5/5_8.png"
            data-lightbox="card5" data-title="떼쓰는 아이 대하는 자세"
        ></a>
        
        <div class="card-news-title">떼쓰는 아이 대하는 자세</div>
  `;

  // 6. 감각통합치료 - 촉각 예민
  const card6 = `
        <a
            href="/static/img/cardnews/card6/6_1.png"
            data-lightbox="card6" data-title="감각통합치료 - 촉각 예민"
        > <img src="/static/img/cardnews/card6/6_1.png" class="card-news-img"/>
        </a>
        <a
            href="/static/img/cardnews/card6/6_2.png"
            data-lightbox="card6" data-title="감각통합치료 - 촉각 예민"
        ></a>
        <a
            href="/static/img/cardnews/card6/6_3.png"
            data-lightbox="card6" data-title="감각통합치료 - 촉각 예민"
        ></a>
        <a
            href="/static/img/cardnews/card6/6_4.png"
            data-lightbox="card6" data-title="감각통합치료 - 촉각 예민"
        ></a>
        <a
            href="/static/img/cardnews/card6/6_5.png"
            data-lightbox="card6" data-title="감각통합치료 - 촉각 예민"
        ></a>
        <a
            href="/static/img/cardnews/card6/6_6.png"
            data-lightbox="card6" data-title="감각통합치료 - 촉각 예민"
        ></a>        
        <div class="card-news-title">감각통합치료 - 촉각 예민</div>
  `;

  // 7. 고유감각
  const card7 = `
        <a
            href="/static/img/cardnews/card7/7_1.png"
            data-lightbox="card7" data-title="고유감각"
        > <img src="/static/img/cardnews/card7/7_1.png" class="card-news-img"/>
        </a>
        <a
            href="/static/img/cardnews/card7/7_2.png"
            data-lightbox="card7" data-title="고유감각"
        ></a>
        <a
            href="/static/img/cardnews/card7/7_3.png"
            data-lightbox="card7" data-title="고유감각"
        ></a>
        <a
            href="/static/img/cardnews/card7/7_4.png"
            data-lightbox="card7" data-title="고유감각"
        ></a>
        <a
            href="/static/img/cardnews/card7/7_5.png"
            data-lightbox="card7" data-title="고유감각"
        ></a>
        <a
            href="/static/img/cardnews/card7/7_6.png"
            data-lightbox="card7" data-title="고유감각"
        ></a>
        <a
            href="/static/img/cardnews/card7/7_7.png"
            data-lightbox="card7" data-title="고유감각"
        ></a>        
        <div class="card-news-title">고유감각</div>
  `;

  // 8. 전정감각
  const card8 = `
        <a
            href="/static/img/cardnews/card8/8_1.png"
            data-lightbox="card8" data-title="전정감각"
        > <img src="/static/img/cardnews/card8/8_1.png" class="card-news-img"/>
        </a>
        <a
            href="/static/img/cardnews/card8/8_2.png"
            data-lightbox="card8" data-title="전정감각"
        ></a>
        <a
            href="/static/img/cardnews/card8/8_3.png"
            data-lightbox="card8" data-title="전정감각"
        ></a>
        <a
            href="/static/img/cardnews/card8/8_4.png"
            data-lightbox="card8" data-title="전정감각"
        ></a>
        <a
            href="/static/img/cardnews/card8/8_5.png"
            data-lightbox="card8" data-title="전정감각"
        ></a>
        <a
            href="/static/img/cardnews/card8/8_6.png"
            data-lightbox="card8" data-title="전정감각"
        ></a>
        <a
            href="/static/img/cardnews/card8/8_7.png"
            data-lightbox="card8" data-title="전정감각"
        ></a>
        <a
            href="/static/img/cardnews/card8/8_8.png"
            data-lightbox="card8" data-title="전정감각"
        ></a>
        <div class="card-news-title">전정감각</div>
  `;

  // 9. 배변훈련
  const card9 = `
        <a
            href="/static/img/cardnews/card9/9_1.png"
            data-lightbox="card9" data-title="배변훈련"
        > <img src="/static/img/cardnews/card9/9_1.png" class="card-news-img"/>
        </a>
        <a
            href="/static/img/cardnews/card9/9_2.png"
            data-lightbox="card9" data-title="배변훈련"
        ></a>
        <a
            href="/static/img/cardnews/card9/9_3.png"
            data-lightbox="card9" data-title="배변훈련"
        ></a>
        <a
            href="/static/img/cardnews/card9/9_4.png"
            data-lightbox="card9" data-title="배변훈련"
        ></a>
        <a
            href="/static/img/cardnews/card9/9_5.png"
            data-lightbox="card9" data-title="배변훈련"
        ></a>
        <a
            href="/static/img/cardnews/card9/9_6.png"
            data-lightbox="card9" data-title="배변훈련"
        ></a>
        <a
            href="/static/img/cardnews/card9/9_7.png"
            data-lightbox="card9" data-title="배변훈련"
        ></a>       
        <div class="card-news-title">배변훈련</div>
  `;

  // 10. 역경 후 성장
  const card10 = `
        <a
            href="/static/img/cardnews/card10/10_1.png"
            data-lightbox="card10" data-title="역경 후 성장"
        > <img src="/static/img/cardnews/card10/10_1.png" class="card-news-img"/>
        </a>
        <a
            href="/static/img/cardnews/card10/10_2.png"
            data-lightbox="card10" data-title="역경 후 성장"
        ></a>
        <a
            href="/static/img/cardnews/card10/10_3.png"
            data-lightbox="card10" data-title="역경 후 성장"
        ></a>
        <a
            href="/static/img/cardnews/card10/10_4.png"
            data-lightbox="card10" data-title="역경 후 성장"
        ></a>
        <a
            href="/static/img/cardnews/card10/10_5.png"
            data-lightbox="card10" data-title="역경 후 성장"
        ></a>
        <a
            href="/static/img/cardnews/card10/10_6.png"
            data-lightbox="card10" data-title="역경 후 성장"
        ></a>        
        <div class="card-news-title">역경 후 성장</div>
  `;

  // 11. 발달장애치료법 골든타임
  const card11 = `
        <a
            href="/static/img/cardnews/card11/11_1.png"
            data-lightbox="card11" data-title="발달장애치료법 골든타임"
        > <img src="/static/img/cardnews/card11/11_1.png" class="card-news-img"/>
        </a>
        <a
            href="/static/img/cardnews/card11/11_2.png"
            data-lightbox="card11" data-title="발달장애치료법 골든타임"
        ></a>
        <a
            href="/static/img/cardnews/card11/11_3.png"
            data-lightbox="card11" data-title="발달장애치료법 골든타임"
        ></a>
        <a
            href="/static/img/cardnews/card11/11_4.png"
            data-lightbox="card11" data-title="발달장애치료법 골든타임"
        ></a>
        <a
            href="/static/img/cardnews/card11/11_5.png"
            data-lightbox="card11" data-title="발달장애치료법 골든타임"
        ></a>
        <a
            href="/static/img/cardnews/card11/11_6.png"
            data-lightbox="card11" data-title="발달장애치료법 골든타임"
        ></a>
        <a
            href="/static/img/cardnews/card11/11_7.png"
            data-lightbox="card11" data-title="발달장애치료법 골든타임"
        ></a>
        <a
            href="/static/img/cardnews/card11/11_8.png"
            data-lightbox="card11" data-title="발달장애치료법 골든타임"
        ></a>
        <a
            href="/static/img/cardnews/card11/11_9.png"
            data-lightbox="card11" data-title="발달장애치료법 골든타임"
        ></a>
        <div class="card-news-title">발달장애치료법 골든타임</div>
  `;

  // 12. 육아스트레스 해소법
  const card12 = `
        <a
            href="/static/img/cardnews/card12/12_1.png"
            data-lightbox="card12" data-title="육아스트레스 해소법"
        > <img src="/static/img/cardnews/card12/12_1.png" class="card-news-img"/>
        </a>
        <a
            href="/static/img/cardnews/card12/12_2.png"
            data-lightbox="card12" data-title="육아스트레스 해소법"
        ></a>
        <a
            href="/static/img/cardnews/card12/12_3.png"
            data-lightbox="card12" data-title="육아스트레스 해소법"
        ></a>
        <a
            href="/static/img/cardnews/card12/12_4.png"
            data-lightbox="card12" data-title="육아스트레스 해소법"
        ></a>
        <a
            href="/static/img/cardnews/card12/12_5.png"
            data-lightbox="card12" data-title="육아스트레스 해소법"
        ></a>       
        <div class="card-news-title">육아스트레스 해소법</div>
  `;

  // 랜덤 6개 숫자(1~12)
  var randomNums = [];
  for (i = 1; i <= 6; i += 1) {
    var rnum = Math.floor(Math.random() * 12) + 1;
    if (randomNums.indexOf(rnum) === -1) {
      randomNums.push(rnum);
    } else {
      i--;
    }
  }

  const component1 = document.getElementById("card-component-1");
  const component2 = document.getElementById("card-component-2");
  const component3 = document.getElementById("card-component-3");
  const component4 = document.getElementById("card-component-4");
  const component5 = document.getElementById("card-component-5");
  const component6 = document.getElementById("card-component-6");

  component1.innerHTML = eval("card" + randomNums[0]);
  component2.innerHTML = eval("card" + randomNums[1]);
  component3.innerHTML = eval("card" + randomNums[2]);
  component4.innerHTML = eval("card" + randomNums[3]);
  component5.innerHTML = eval("card" + randomNums[4]);
  component6.innerHTML = eval("card" + randomNums[5]);
});
