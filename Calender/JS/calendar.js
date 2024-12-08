function toEnglishDigits(num) {

  const id = {
    '۰': '0',
    '۱': '1',
    '۲': '2',
    '۳': '3',
    '۴': '4',
    '۵': '5',
    '۶': '6',
    '۷': '7',
    '۸': '8',
    '۹': '9',
  }
  return num ? num.toString().replace(/[^0-9.]/g, function (w) {
    return id[w] || w
  }) : null

}

function toPersianDigits(num) {
  const farsiDigits = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];

  return num
      .toString()
      .replace(/\d/g, x => farsiDigits[x]);
}

var selectedYearIndex = (calendarData.years.length-1);
var selectedMonthIndex = -1;
var selectedDayIndex = -1;
let pointedDate = false;

// ایجاد Combo Box برای انتخاب ماه
const yearSelector = document.getElementById("yearSelector");

calendarData.years.forEach((year, index) => {
    const option = document.createElement("option");
    option.value = index;
    option.textContent = toPersianDigits(year.year);
    yearSelector.appendChild(option);
});

yearSelector.onchange = function() {
  selectedYearIndex = yearSelector.options[yearSelector.selectedIndex].value; 
}

const monthSelector = document.getElementById("monthSelector");

calendarData.years[selectedYearIndex].months.forEach((month, index) => {
    const option = document.createElement("option");
    option.value = index;
    option.textContent = month.name;
    monthSelector.appendChild(option);
});


let today = new Date().toLocaleDateString('fa-IR');

calendarData.years.forEach((year,index) =>{
  if (toEnglishDigits(today.split("/")[0]) == year.year){
    selectedYearIndex = index;
    yearSelector.selectedIndex = selectedYearIndex;
    year.months.forEach((month, index) =>{
      if(toEnglishDigits(today.split("/")[1]) == month.number){
        selectedMonthIndex = index;
        monthSelector.selectedIndex = selectedMonthIndex;
        month.days.forEach((day,index) => {
          if(toEnglishDigits(today.split("/")[2]) == day.date){ 
            selectedDayIndex = index;
          }
        })
      }
    })
  }
})

function clickedDay(dayIndex){
  selectedDayIndex = dayIndex;
  pointedDate = true;
  renderCalendar(selectedYearIndex,selectedMonthIndex);
}

// نمایش تقویم
function renderCalendar(yearIndex,monthIndex) {
  
  yearSelector.selectedIndex = yearIndex;
  monthSelector.selectedIndex = monthIndex;
  
  const month = calendarData.years[yearIndex].months[monthIndex];
  
  let calendarHTML = `<div class="daysOfWeek">
                        <div>ش</div>
                        <div>ی</div>
                        <div>د</div>
                        <div>س</div>
                        <div>چ</div>
                        <div>پ</div>
                        <div>ج</div>
                      </div>
                      <div class="datesOfWeek">
                        <div class="eachWeek">`;

  // پیدا کردن روز جمعه اول ماه
  const firstFridayIndex = month.days.findIndex(day => day.isFriday);

  for(let i = 0; i < (7-(firstFridayIndex+1)); i++){
      calendarHTML += `<div class="eachDate"></div>`;
  }

  month.days.forEach((day,index) => {

    const isTodayClass =(toEnglishDigits(today.split("/")[0]) == calendarData.years[yearIndex].year) && 
                  (toEnglishDigits(today.split("/")[1]) == calendarData.years[yearIndex].months[monthIndex].number) && 
                  (toEnglishDigits(today.split("/")[2]) == day.date) ? 'today' : ''; 

    const isFridayClass = day.isFriday || day.isHoliday ? 'friday' : 'eachDate';
    const isPointedDay = pointedDate && (selectedDayIndex == index) ? 'pointed' : '';
  
    calendarHTML += ` <div class="${isFridayClass} ${isTodayClass} ${isPointedDay}" onclick="clickedDay(${index})">
                          <div class="iranDate">${toPersianDigits(day.date)}</div>
                          <div class="otherDates">
                              <div class="gregorian">${day.gregorian.date}</div>
                              <div class="hijri">${toPersianDigits(day.hijri.date)}</div>
                          </div>
                      </div>`;

    // اگر به جمعه رسیدیم، ردیف را ببندیم و یک ردیف جدید شروع کنیم
    if (day.isFriday) {
        calendarHTML += `</div><div class="eachWeek">`;
    }
    
  });

  let lastFridayIndex = -1;

  for(let j = (month.days.length - 1); j >= 0; j--){
    if(month.days[j].isFriday){
      lastFridayIndex = j;
      break;
    }
  }

  let daysAfterLastFriday = (month.days.length - 1)-(lastFridayIndex)

  if(!(daysAfterLastFriday == 0)){
    for(let k = 0; k < 7-(daysAfterLastFriday); k++){
      calendarHTML += `<div class="eachDate"></div>`;
    }
  }

  calendarHTML += "</div></div>";
  document.getElementById("calendar").innerHTML = calendarHTML;
  
  document.getElementById("dateData").innerHTML = toPersianDigits(calendarData.years[yearIndex].months[monthIndex].days[selectedDayIndex].date) + " ";
  
  let gregorianStart = calendarData.years[yearIndex].months[monthIndex].days[0].gregorian.month;
  let gregorianFinish = calendarData.years[yearIndex].months[monthIndex].days[calendarData.years[yearIndex].months[monthIndex].days.length-1].gregorian.month;
  let gregorianYear = calendarData.years[yearIndex].months[monthIndex].days[0].gregorian.year;
  
  let hijriStart = calendarData.years[yearIndex].months[monthIndex].days[0].hijri.month;
  let hijriFinish = calendarData.years[yearIndex].months[monthIndex].days[calendarData.years[yearIndex].months[monthIndex].days.length-1].hijri.month;
  let hijriYear = calendarData.years[yearIndex].months[monthIndex].days[0].hijri.year;
  
  let monthDataHtml = `<div>${gregorianStart} to ${gregorianFinish} in ${gregorianYear}</div>
                       <div>${hijriStart} to ${hijriFinish} in ${hijriYear}</div>`;
  
  document.getElementById('monthData').innerHTML = monthDataHtml;

}

// بارگذاری تقویم اولیه و ایجاد Event Listener برای Combo Box
renderCalendar(selectedYearIndex,selectedMonthIndex);

yearSelector.addEventListener("change", (event) => {
  selectedYearIndex = event.target.value; 
  renderCalendar(selectedYearIndex,selectedMonthIndex);
});

monthSelector.addEventListener("change", (event) => {
  selectedMonthIndex =event.target.value;
  renderCalendar(selectedYearIndex,selectedMonthIndex);
});


document.getElementById("previousMonth").addEventListener("click",() => {
  selectedMonthIndex --;
  renderCalendar(selectedYearIndex,selectedMonthIndex);
})

document.getElementById("nextMonth").addEventListener("click",() => {
  selectedMonthIndex ++;
  renderCalendar(selectedYearIndex,selectedMonthIndex);
})