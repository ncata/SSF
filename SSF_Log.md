# Nick Catanzaro 2021 SSF Activity Log  

## 06/03/21  
* 9am-10:20am: Meeting with Dr. Sherwood. Set up Github and installed/tried out Git.   
* 10:20am-12:00pm: Completed WHOI Conflict of Interest form and began filling out remaining WHOI Orientation paperwork.
* 12:00pm-12:45pm: Lunch
* 12:45pm-2:25pm: Respond to emails and continue filling out paperwork, collect keys to MSU campus lab
* 2:25pm-5:30pm: MATLAB Onramp training, Doodler install under "/njc/src/dash_doodler/dash_doodler", and more emails/paperwork  

## 06/04/21
* 9am-10am: Experiment with Doodler and set up payroll.
* 10am-11am: Literature review of "Remote Sensing of the Nearshore" (Holman and Haller, 2013) and "SurfRCaT: A tool for remote calibration of pre-exsitiing coastal cameras to enable their use as quantitative coastal monitoring tools" (Conlin et al., (2020).
* 11am-12pm: MATLAB Onramp training
* 12pm-1pm: WHOI Allyship Panel
* 1pm-2pm: Lunch
* 2pm-3pm: Reef Solutions Seminar
* 3pm-4pm: SSF Virtual Social

## 06/07/21  
* 9am-10am: Meeting with Chris Sherwood. Recorded weekly to do list. Installed Irfan Viewer and bookmarked nbviewer.
* 10am-11am: Review MI City NOAA GLERL webpage. Noted that coordinates provided are not precise enough to point to current or past webcam placement. Identified View 1 image 9 (06/06/2021 19:03 EDT) as shifting relative to images 8 and 10 in the 06/06/2021 12-hour animation. Noted disparity between archived image time and the time displayed on the image itself-probably the time between the photo being taken versus the time the photo was uploaded. First several photos in the 10 day archive were not accessible.
* 11am-2pm: Created a jupyter notebook for practicing aligning images from the MI City lighthouse. Took a lunch break during that time.
* 2pm-3pm: Reviewed SurfRCat paper 'SurfRCat: A tool for remote calibration of pre-exsisting coastal cameras to enable their use a quantitative coastal monitoring tools" (Conlin et al., 2020). More precise data regarding lat, lon, elevation, and azimuth of GLERL webcams would be needed by LiDAR data should be available.
* 3pm-5pm: Reauthorized ArcGIS 10.7.1 licencse and created a rudimentary map showing the MI City GLERL webcam view #1. Continued reviewing GLERL webpage and exploring links-still unable to find archived photos past previous 10 days. Looked through SurfRCat repository again.
* 5pm-6pm: MATLAB Onramp training and reading chapters 1 and 2 of Pro Git.  

## 06/08/2021
* 9am-10am: eQIP online background check
* 10am-11am: Started lit reveiw of Argus stations
* 11am-12:30pm: Woods Hole USGS Center Meeting
* 1pm-2pm: Coastal Change and Hazards Group Seminar (Both meetings had great talks!)
* 3:30pm-4:30pm: Finished Argus lit review
* 4:30pm-6:30pm: MATLAB Onramp training/troubleshooting git error (Must remember to be update my local SSF_Log file before pulling changes I made remotely or vice versa)

## 06/09/2021
* 9am-9:30am: Finished MATLAB Onramp training and reviewed provided course summaries.
* 9:30am-11am: Updated calendar on outlook and continued practicing manipulating images using matplotlib and PIL in python on the Image_analysis_practice.ipynb.
* 11am-12:10pm: SSF lecture, Ocean Heat Transfer and Arctic Amplification. (Super cool!)
* 1pm-2pm: Emails, webinar registration, walked to Hardisty lab.
* 2pm-2:30pm: Hardisty Lab Tour.
* 2:30pm-3pm: Installed R, Rstudio, and Jupyter Lab for the upcoming data science workshops.
* 3pm-5:30pm: Explored GLERL data products, metadata, Muskegon Webcam images, and searched for/noted surfcams not maintained by GLERL that could be used in SurfRCaT.
* 7:30pm-9pm: Ocean Twilight Zone Webinar and SSF science communications discussion.

## 06/10/2021
* 9am-11am: Meeting with Chris Sherwood. Recorded to-do list and began making the rgb2gray function in jupyter notebook. Must find how PIL uses grayscale (luminosity possibly)
* 11am-12pm: Reviewed Great Lakes Environmental Research Laboratory (GLERL) Lake Michigan Field Station (LMFS) information. LMFS is located in Muskegon, MI. Based on the potential of support from GLERL due to 12 resident staff, proximity to Lansing, and webcam position(s) this is currently the \#1 field site prospect. Calibrated tech.
* 1pm-2pm: Began working with .las files showing area surrounding LMFS from NOAA Digital Coast Dataviewer in CloudCompare. Began cross-referencing .las files with Google Earth Imagery. Briefly read USGS UTM fact sheet to re-familiarize myself with UTM coordinates/false northings.
* 2pm-3:30pm: Machine Learning group meeting. Focus on condensing tools and increasing access for non-academic managers was really cool.
* 3:30pm-5:35pm: Found an image of the LMFS com tower (alleged location of webcam). It seems offset from where I would have expected it to be based on images from View \#1. Completed CloudCompare tutorial. Ordered more .las files. Charted locations in my notes of points that I will use to attempt to derive the horizontal angle/potentially elevation of webcams with.

## 06/11/2021
* 9am-11am: SurfRCat review and tutorial. Must try at home with a wired internet connection to see if that helps at the "sorting tiles" phase of lidar download.
* 11am-12pm: Notes on formulas and background information related to calculating a camera's horizontal angle of view (HAOV)
* 12:30pm-1:30pm: Began researching and recording different ways of comparing two images in order to write an error metric function.
* 1:30pm-2pm: SSF Meetup
* 2pm-4pm: Reviewed stack overflow pages and the guides of PIL, matplotlib, SciPy, and sys to find useful modules and understand the code that was being recommended by stack overflow users. Read about transformation matrices.
* 4pm-5pm: Compiled information in notes and tried to troubleshoot Git issue. It seems as if a file is stuck in the limbo of being committed even though it is no longer tracked and there are commands to remove the file also committed. Ultimately, Git is rejecting all push commands because a .las file exceeding 200mb is present in the files being pushed to Github.

## 06/12/21
* 12pm-12:30pm: Resolved git issue by resetting branch and reupdating SSF_Log
* 12:30pm-4pm: Researched image translation, cross correlation, and began trying out code and writing functions in the jupyter notebook

## 06/13/21
* 12:30pm-11pm (total working time ~6.5 hours): Reworked functions until all code returned with no errors. Was not able to accurately guess quiz image translations. the stooges function is held back by the black background that occurs during image translation in openCV. I am not sure why plot_corr is not working, but it may be that the scipy.signal.correlation2d() function sees too much similarity across the images.  

## 06/14/21
* 9am-10:30am: Meeting with Dr. Sherwood. Received weekly to do list and revealed/reviewed image alignment code.
* 10:30am-12pm: cloned coastcam.py and coastcamfuncs and pulled updates to SSF_2021 and dash_doodler repos. Reviewed CIRN Understanding Image Geometrics Photogrammetry section.
* 12:30pm-1:15pm: Completed notes on Photogrammetry.
* 1:30pm-4pm: WHOI Software Carpentry Python Workshop: Went over using git bash and bash commands. Learned a few new tricks and had good review/background on how git works on basic level.
* 4pm-5pm: Installed Hydrogen package for Atom. Wrote questions and sorted them by importance (primary, secondary, tertiary) for Steve Ruberg meeting on Thursday morning. Filled out tentative hourly schedule for upcoming week.

## 06/15/21
* 9am-11am: Email updates, wrote image translation registration function in a .py file to test __main__ functions, read about the application of __main__ functions.
* 2pm-3pm: GLERL Muskegon station metadata review. Found the "hidden" view \#6 in the past 10 days webpage. Located the beach as being a zoomed in view south of the harbor.
* 3pm-4pm: Downloaded Muskegon GLERL images and made a presentation. Updated Muskegon LMFS notes. Made a few very fast "maps" from downloaded Google Earth images, did a quick dry run of slides content and review of webcam notes to prep for CoastCam meeting.
* 4pm-5pm: CoastCam meeting. Introductions, what we want to learn from the group over the summer, and GL camera slides. Jenna brought up optical wave gauging as a potential use for the cameras. Muskegon could be a good test site because it has a ReCON buoy that collects wave data offshore of the cameras at a depth of 72 feet. This could be used to test the model.
* 5pm-6pm: Renewed scouting of ReCON researched infrastructure, looking specifically for what buoys collected wave data. Must remember to make a new notes page to record this information. Thunder Bay island ReCON station has very interesting views of a rocky beach with a rock "bar" ("shoal?" must brush up on my coastal morphology) likely no deeper than chest depth. However, access to this site is difficult due to the necessity of a watercraft for access and distance from Lansing. Could be worth discussing with Dr. Sherwood/Steve Ruberg. MSU GEO dept.'s Theuerkauf Lab does have a boat on GLs. Fall research is in Lake Huron so I could try and reach out and see if the lab has already collected any data that could be useful/has plans to do so this summer.
* 6pm-7pm: Set up defensive drivers course and got translation function to run, however it is not properly displaying the __main__ output in jupyter notebook so I will make a new notebook tomorrow to see if that will work better.

## 06/16/2021
* 9am-11am: Update SSF_Log, respond to emails, meeting with Chris Sherwood to discuss questions for meeting with Steve Ruberg tomorrow at 9am.
* 11am-12pm: SSF Lecture-The Ocean Observatories Initiative (OOI): Building and deploying moorings to make long term measurements in the ocean. Very interesting talk about a variety of ocean observation systems, career paths, and sensors/monitors.
* 12:30pm-1pm: Drafted email with questions and my background for Steve Ruberg.
 * 1pm-3:30pm: WHOI Software Carpentry Python workshop. Wrapped up bash and began basic parts of python indexing and using jupyter.
 * 3:30pm-5pm: Emailed Sheri White about her talk and to see if I could have some of the figures for my personal notes, set up meeting about professional development with another SSF, watched R/V Neil Armstrong 2016 cruise video.
 * 5pm-6pm: Livestream about ocean exploration work occurring in Thunder Bay National Marine Sanctuary (most of Lake Huron is not mapped to resolution < 80m).
 * 6pm-7:30pm: Defensive driving courese certification (100% final exam accuracy on 1 attempt), final emails.

## 06/17/2021
* 9am-10am: Meeting with Steve Ruberg and Chris Sherwood. Access to ReCON archives is approved pending selection of an appropriate delivery method via either a hard drive or a cloud service. Chance of touring GLERL headquarters and/or doing field work with NOAA is a possibility.
* 10am-11am: Updated notes from CIRN's Image Processing-Photogrammetry section. Drafted a follow up email for Steve.
* 11am-12pm: Went over abstracts of optical wave gauge and run up papers. Prepped them for printing through MSU library.
* 12:30-1:00pm: Spoke with other SSFs about using NumPy interpolation functions, applications of GIS/RS, using MATLAB/MATLAB software carpentry workshop days, and introduced myself to new fellows and discussed our research topics.
* 1pm-2pm: Looked over slides from yesterdays presentation and followed links that Sheri White sent me.
* 2pm-5pm: Printed papers in MSU library and began annotating the Stockton reading.

## 06/18/2021
* 9:30am-10am: Update SSF_Log and review emails, tasks to be completed ahead of next week, and the days schedule.
* 10am-11am: Complete notes on CIRN Data Processing Image Geometrics library. Reviewed CoastCam repo functions.
* 12pm-12:30: Continued familiarizing myself with CoastCam functions.
* 1pm-2pm: SSF call about careers and finding jobs outside of traditional research.
* 2pm-3pm: Began annotating "Optical wave gauging using deep neural networks" (Buscombe et al, 2019)
* 3pm-4pm: WHOI/MIT JP Jelly talks.
* 4pm-6pm: SSF Trivia Night on gather.town.
