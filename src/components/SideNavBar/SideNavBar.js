import React,{useState, useEffect} from 'react';
import classes from './SideNavBar.module.css';
import SideNavBarButton from './SideNavBarButton';


import { BsChatLeftText,BsUiChecksGrid,BsPencilSquare,BsPeople,
	BsFilePerson,BsHammer,BsBook,BsChatDots,BsFillCameraReelsFill, 
        BsCameraReels} from "react-icons/bs";
import {BsGraphUp,BsZoomIn,BsTrophy,BsListOl,BsCalendarDay,BsQuestionSquare,BsReverseLayoutTextSidebarReverse} from 'react-icons/bs';
import {GiTeacher} from "react-icons/gi";
import { useNavigate } from "react-router-dom";







const SideNavBar=(props)=>{

   let history = useNavigate();
   let inActivebuttonColor="var(--sideNavBarBkgColor)";




   const [sideNavBarWidth, setSideNavBarWidth] = useState(props.sideNavBarWidth);


   

   const [dashboardButtonColor, setDashoardButtonColor]=useState(inActivebuttonColor);
   const [courseButtonColor, setCourseButtonColor]=useState(inActivebuttonColor);

   const [messagesButtonColor, setMessagesButtonColor]=useState(inActivebuttonColor);	
   
   const [discussionButtonColor, setDiscussionButtonColor]=useState(inActivebuttonColor);

   const [classButtonColor, setClassButtonColor]=useState(inActivebuttonColor);  
   const [tasksButtonColor, setTasksButtonColor]=useState(inActivebuttonColor);
   const [booksButtonColor, setBooksButtonColor]=useState(inActivebuttonColor);
   const [examButtonColor, setExamButtonColor]=useState(inActivebuttonColor);
   const [classmatesButtonColor, setClassmatesButtonColor]=useState(inActivebuttonColor);
   const [teacherButtonColor, setTeacherButtonColor]=useState(inActivebuttonColor);	
   const [prepareButtonColor, setPrepareButtonColor]=useState(inActivebuttonColor);
   const [progressButtonColor, setProgressButtonColor]=useState(inActivebuttonColor);
   const [analyticsButtonColor, setAnalyticsButtonColor]=useState(inActivebuttonColor);

   const [achievementsButtonColor, setAchievementsButtonColor]=useState(inActivebuttonColor);

   const [gradesButtonColor, setGradesButtonColor] = useState(inActivebuttonColor);

   const [goalsButtonColor, setGoalsButtonColor]=useState(inActivebuttonColor);
   const [calenderButtonColor, setCalenderButtonColor]=useState(inActivebuttonColor);
   const [diaryButtonColor, setDiaryButtonColor]=useState(inActivebuttonColor);
   const [helpcenterButtonColor, setHelpCenterButtonColor]=useState(inActivebuttonColor)



   useEffect(() => {
     setSideNavBarWidth(props.sideNavBarWidth);
   }, [props.sideNavBarWidth]);




   useEffect(()=>{

        let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
        let inActivebuttonColor="var(--sideNavBarBkgColor)";
    
        !props.dashboardMounted && setDashoardButtonColor(dashboardButtonColor=>inActivebuttonColor);
	props.dashboardMounted && setDashoardButtonColor(dashboardButtonColor=>activeButtonColor);    


   },[props.dashboardMounted]);


  useEffect(()=>{

        let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
        let inActivebuttonColor="var(--sideNavBarBkgColor)";

        !props.courseMounted && setCourseButtonColor(courseButtonColor=>inActivebuttonColor);
        props.courseMounted && setCourseButtonColor(courseButtonColor=>activeButtonColor);


   },[props.courseMounted]);











   useEffect(()=>{ 
       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";

       !props.messagesMounted && setMessagesButtonColor(messagesButtonColor=>inActivebuttonColor);
       props.messagesMounted && setMessagesButtonColor(messagesButtonColor=>activeButtonColor); 	   

   },[props.messagesMounted]);


   useEffect(()=>{
       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";

       !props.discussionMounted && setDiscussionButtonColor(discussionButtonColor=>inActivebuttonColor);
       props.discussionMounted && setDiscussionButtonColor(discussionButtonColor=>activeButtonColor);

   },[props.discussionMounted]);





   useEffect(()=>{

       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";

       !props.classMounted && setClassButtonColor(classButtonColor=>inActivebuttonColor);
       props.classMounted && setClassButtonColor(classButtonColor=>activeButtonColor);

   },[props.classMounted]);
  

  useEffect(()=>{
      let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
      let inActivebuttonColor="var(--sideNavBarBkgColor)";


      !props.tasksMounted && setTasksButtonColor(tasksButtonColor=>inActivebuttonColor);
      props.tasksMounted && setTasksButtonColor(tasksButtonColor=>activeButtonColor);

   },[props.tasksMounted]);


   useEffect(()=>{

        let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
        let inActivebuttonColor="var(--sideNavBarBkgColor)";


        !props.booksMounted && setBooksButtonColor(booksButtonColor=>inActivebuttonColor);
        props.booksMounted && setBooksButtonColor(booksButtonColor=>activeButtonColor);

   },[props.booksMounted]);


   useEffect(()=>{

       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";


       !props.examMounted && setExamButtonColor(examButtonColor=>inActivebuttonColor);
       props.examMounted && setExamButtonColor(examButtonColor=>activeButtonColor);

   },[props.examMounted]);

   useEffect(()=>{

       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";


       !props.classmatesMounted && setClassmatesButtonColor(classmatesButtonColor=>inActivebuttonColor);
       props.classmatesMounted && setClassmatesButtonColor(classmatesButtonColor=>activeButtonColor);

   },[props.classmatesMounted]);


   useEffect(()=>{

       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";



      !props.teacherMounted && setTeacherButtonColor(teacherButtonColor=>inActivebuttonColor);
      props.teacherMounted && setTeacherButtonColor(teacherButtonColor=>activeButtonColor);

   },[props.teacherMounted]);


   useEffect(()=>{
       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";

       !props.prepareMounted && setPrepareButtonColor(prepareButtonColor=>inActivebuttonColor);
       props.prepareMounted && setPrepareButtonColor(prepareButtonColor=>activeButtonColor);

   },[props.prepareMounted]);


   useEffect(()=>{

       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";



      !props.progressMounted && setProgressButtonColor(progressButtonColor=>inActivebuttonColor);
      props.progressMounted && setProgressButtonColor(progressButtonColor=>activeButtonColor);

   },[props.progressMounted]);


   useEffect(()=>{

       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";



      !props.analyticsMounted && setAnalyticsButtonColor(analyticsButtonColor=>inActivebuttonColor);
      props.analyticsMounted && setAnalyticsButtonColor(analyticsButtonColor=>activeButtonColor);

   },[props.analyticsMounted]);	


   useEffect(()=>{
       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";



      !props.achievementsMounted && setAchievementsButtonColor(achievementsButtonColor=>inActivebuttonColor);
      props.achievementsMounted && setAchievementsButtonColor(achievementsButtonColor=>activeButtonColor);

   },[props.achievementsMounted]);


   useEffect(()=>{

       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";



      !props.goalsMounted && setGoalsButtonColor(goalsButtonColor=>inActivebuttonColor);
      props.goalsMounted && setGoalsButtonColor(goalsButtonColor=>activeButtonColor);

   },[props.goalsMounted]);


   useEffect(()=>{
      let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
      let inActivebuttonColor="var(--sideNavBarBkgColor)";



      !props.calenderMounted && setCalenderButtonColor(calenderButtonColor=>inActivebuttonColor);
      props.calenderMounted && setCalenderButtonColor(calenderButtonColor=>activeButtonColor);

   },[props.calenderMounted]);


   useEffect(()=>{
       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";



      !props.diaryMounted && setDiaryButtonColor(diaryButtonColor=>inActivebuttonColor);
      props.diaryMounted && setDiaryButtonColor(diaryButtonColor=>activeButtonColor);

   },[props.diaryMounted]);



   useEffect(()=>{

       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";


       !props.gradesMounted && setGradesButtonColor(gradesButtonColor=>inActivebuttonColor);
       props.gradesMounted && setGradesButtonColor(gradesButtonColor=>activeButtonColor);

   },[props.gradesMounted]);














   useEffect(()=>{

       let activeButtonColor="linear-gradient(to right, var(--sideNavBarBtnhoverColor) 90%, var(--themeColor) 0%)";
       let inActivebuttonColor="var(--sideNavBarBkgColor)";



      !props.helpcenterMounted && setHelpCenterButtonColor(helpcentreButtonColor=>inActivebuttonColor);
      props.helpcenterMounted && setHelpCenterButtonColor(helpcentreButtonColor=>activeButtonColor);

   },[props.helpcenterMounted]);






   const dashboardHandler=()=>{
   props.rerender();
   if(props.userData.usertype===4){	   
   history.push('/dashboard/employee');
   }else{

   localStorage.removeItem('preferredCourseId');
   history.push('/dashboard/general');

   }	   
   	   
   }

   const courseSummaryHandler =()=>{

   history.push('/course/summary');

   }


   const courseGradesHandler=()=>{

   history.push('/course/grades');

   }	   



   

  const discussionHandler=()=>{
  history.push('/messages/tickets');

  }



   const messagesHandler=()=>{
   history.push('/course/chat');
   }

   const classHandler=()=>{
   history.push('/course/classes');
   }

   const tasksHandler=()=>{
   history.push('/assignment/home');
   }	

   const booksHandler=()=>{
   history.push('/books/findbook');
   }

   const examHandler=()=>{
   history.push('/course/exams');
   }

   const classmatesHandler=()=>{
   history.push('/students/all');
   }

   const teacherHandler=()=>{
   history.push('/course/teacher');
   }

   const prepareHandler=()=>{
   history.push('/prepare');
   }
   
   const progressHandler=()=>{
   history.push('/progress');
   }

   const analyticsHandler=()=>{
   history.push('/analyics');
   }

   const achievementsHandler=()=>{
   history.push('/meetings/overview');
   }

   const goalsHandler=()=>{
   history.push('/goals');
   }

   const calenderHandler=()=>{
   history.push('/calender');
   }


   const diaryHandler=()=>{
   history.push('/diary');
   }

   const helpCenterHandler=()=>{
   history.push('/helpcenter');
   }










   return (

     <div className={classes.SideMainContainer} style={{width:sideNavBarWidth}} >

        {/*
        <SideNavBarButton onPress={dashboardHandler}   
	   icon={BsSpeedometer} 
	   name="Dashboard" 
	   buttonColor={{background:dashboardButtonColor }}/>
         */}


        <SideNavBarButton onPress={courseSummaryHandler}  icon={BsReverseLayoutTextSidebarReverse} name="Summary" buttonColor={{background:courseButtonColor }}/>




        <SideNavBarButton onPress={messagesHandler}  icon={BsChatDots} name="Chat" buttonColor={{background:messagesButtonColor }}/>

        <SideNavBarButton onPress={discussionHandler}  icon={BsChatLeftText} name="Discussion" buttonColor={{background:discussionButtonColor }}/>


        <SideNavBarButton onPress={classHandler} icon={GiTeacher} name="Classes" buttonColor={{background:classButtonColor }} />

        <SideNavBarButton onPress={tasksHandler} icon={BsUiChecksGrid} name="Assignments"buttonColor={{background:tasksButtonColor }} />

        <SideNavBarButton onPress={booksHandler} icon={BsBook} name="Books"  buttonColor={{background:booksButtonColor }} />

        <SideNavBarButton onPress={examHandler} icon={BsPencilSquare} name="Exam"  buttonColor={{background:examButtonColor }} />

        <SideNavBarButton onPress={classmatesHandler} icon={BsPeople} name="Students"  buttonColor={{background:classmatesButtonColor }} />	

        <SideNavBarButton onPress={teacherHandler} icon={BsFilePerson} name="Teacher"  buttonColor={{background:teacherButtonColor }} />

        <SideNavBarButton onPress={prepareHandler} icon={BsHammer} name="Prepare"  buttonColor={{background:prepareButtonColor }} />

        <SideNavBarButton onPress={progressHandler} icon={BsGraphUp} name="Progress"  buttonColor={{background:progressButtonColor }} />

        <SideNavBarButton onPress={analyticsHandler} icon={BsZoomIn} name="Analytics"  buttonColor={{background:analyticsButtonColor }} />	

        <SideNavBarButton onPress={achievementsHandler} icon={BsCameraReels} name="Meetings"  buttonColor={{background:achievementsButtonColor }} />

        <SideNavBarButton onPress={courseGradesHandler}  icon={BsReverseLayoutTextSidebarReverse} name="Grades" buttonColor={{background:gradesButtonColor }}/>

	<SideNavBarButton onPress={goalsHandler} icon={BsListOl} name="Goals"  buttonColor={{background:goalsButtonColor }} />	
        {/*
        <SideNavBarButton onPress={calenderHandler} icon={BsCalendarDay} name="Calender"  buttonColor={{background:calenderButtonColor }} />

        <SideNavBarButton onPress={diaryHandler} icon={BsJournalText} name="Diary"  buttonColor={{background:diaryButtonColor }} />

        <SideNavBarButton onPress={helpCenterHandler} icon={BsQuestionSquare} name="Help Center"  buttonColor={{background:helpcenterButtonColor }} />
        */}

     </div>

   );




}




export default SideNavBar;

