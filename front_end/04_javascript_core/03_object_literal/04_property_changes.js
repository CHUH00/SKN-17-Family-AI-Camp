/* 프로퍼티 값 추가, 수정, 삭제 */

/*
    - 존재하지 않는 프로퍼티에 접근해서 값을 대입 > 추가
    - 존재하는 프로퍼티에 접근해서 값을 대입 > 수정
    - delete 키워드를 이용해 프로퍼티에 접근 > 삭제
      (이때 존재하지 않는 프로퍼티를 넣어도 에러 없이 무시됨)
*/

var kitty = {
    name: '나비'
};

// 추가
kitty['zipsa'] = '태연';
kitty.like = '츄르';
console.log(kitty);

// 수정
kitty.name = '보리';
kitty['like'] = '태연';
console.log(kitty);

// 삭제
delete kitty.like;
delete kitty['zipsa'];
delete kitty.age;
delete kitty['house'];
console.log(kitty);
