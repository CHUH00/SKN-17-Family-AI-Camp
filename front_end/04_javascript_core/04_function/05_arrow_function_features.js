/* 화살표 함수의 특징 */

// 1. 화살표 함수는 this를 가지지 않는다.
var theater = {
    store: '영등포점',
    titles: ['어쩔수가없다', '극장판 체인소 맨', '극장판 귀멸의 칼날', '얼굴', 'F1 더 무비'],
    showMovieList() {
        this.titles.forEach(
            title => console.log(this.store + ":" + title)
            // function(title) {
            //     console.log(this.store + ":" + title);
            // }
        );
    }
};

theater.showMovieList();

// 2. 화살표 함수는 new와 함께 호출할 수 없다.

// 3. 화살표 함수는 super를 가지지 않는다.

// 4. 화살표 함수는 arguments를 지원하지 않는다.
(function() {
    // var arrowFunc = function() {
    //     console.log(arguments);
    // }
    var arrowFunc = () => console.log(arguments);
    arrowFunc(3, 4);
}(1, 2));
