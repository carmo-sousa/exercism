//
// This is only a SKELETON file for the 'Resistor Color Duo' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const decodedValue = (color_list) => {
  
  const color = {
    black: 0,
    brown: 1,
    red: 2,
    orange: 3,
    yellow: 4,
    green: 5,
    blue: 6,
    violet: 7,
    grey: 8,
    white: 9
  }

  let color_1 = color_list[0]
  let color_2 = color_list[1]

  return parseInt([color[color_1], color[color_2]].join(''))
};
