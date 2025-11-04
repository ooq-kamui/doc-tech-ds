
const a = {
  key01 : 'aaa01',
  key02 : 'aaa02',
}


if ('key01' in a){
  console.log(true)
}

if ('toString' in a){
  console.log(true)
}


if (a.hasOwnProperty('toString')){
  console.log(true)
}



