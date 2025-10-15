/* method */

// 메서드를 정의하려면 프로퍼티 값으로 함수를 할당 (ES5)
var puppy = {
    name: '뽀삐',
    eat: function(food) {
        console.log(`${this.name}은(는) ${food}를 맛있게 먹어요~!`);
    }
};

puppy.eat('소고기');



/* 메서드 값 단축 구문 (ES6) */
var squirrel = {
    name: '람쥐썬더',
    action(skill) {
        console.log(`${this.name}이(가) ${skill}을(를) 보여줍니다!`);
    }
};

squirrel.action('현란한 강의');
