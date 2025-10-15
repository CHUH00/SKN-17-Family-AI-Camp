/* strict mode 활용 */

// 1. 암묵적 전역 방지
(function(){
    // 'use strict';
    x = 1;
}());
console.log(x);



// 2. 매개변수 이름 중복 방지
(function(){
    // 'use strict';
    function test(x, x) {
        return x + x;
    }

    console.log(test(1, 2));
}());



// 3. 변수, 함수, 매개변수의 삭제 방지 (delete 키워드 사용 에러)
(function(){
    // 'use strict';
    var y = 1;
    delete y;
    console.log(y);
}());



// 4. with문 사용 방지
(function(){
    // 'use strict';
    with({ z : 1 }) {
        console.log(z);
    }
}());



// 5. 일반 함수에서의 this 사용 제한
// - 일반 함수로서 호출한 함수의 this == 전역 객체
// - strict mode에서 일반 함수로서 호출한 함수의 this == undefined
(function(){
    'use strict';
    function testThis() {
        console.log(this);
    }
    testThis();
    new testThis();
}());



// 6. arguments 객체
// strict mode에서는 매개변수에 전달된 인수를 재할당해 변경해도
// arguments 객체에는 반영되지 않음
(function(arg){
    'use strict';
    arg = 1;

    console.log(arg);
    console.log(arguments);
}(777));
