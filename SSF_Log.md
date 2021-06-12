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
* 11am-12pm: Reviewed Great Lakes Environmental Research Laboratory (GLERL) Lake Michigan Field Station (LMFS) information. LMFS is located in Muskegon, MI. Based on the potential of support from GLERL due to 12 resident staff, proximity to Lansing, and webcam position(s) this is currently the /#1 field site prospect. Calibrated tech.
* 1pm-2pm: Began working with .las files showing area surrounding LMFS from NOAA Digital Coast Dataviewer in CloudCompare. Began cross-referencing .las files with Google Earth Imagery. Briefly read USGS UTM fact sheet to re-familiarize myself with UTM coordinates/false northings.
* 2pm-3:30pm: Machine Learning group meeting. Focus on condensing tools and increasing access for non-academic managers was really cool.
* 3:30pm-5:35pm: Found an image of the LMFS com tower (alleged location of webcam). It seems offset from where I would have expected it to be based on images from View /#1. Completed CloudCompare tutorial. Ordered more .las files. Charted locations in my notes of points that I will use to attempt to derive the horizontal angle/potentially elevation of webcams with.

## 06/11/2021
* 9am-11am: SurfRCat review and tutorial. Must try at home with a wired internet connection to see if that helps at the "sorting tiles" phase of lidar download.
* 11am-12pm: Notes on formulas and background information related to calculating a camera's horizontal angle of view (HAOV)
* 12:30pm-1:30pm: Began researching and recording different ways of comparing two images in order to write an error metric function.
* 1:30pm-2pm: SSF Meetup
* 2pm-4pm: Reviewed stack overflow pages and the guides of PIL, matplotlib, SciPy, and sys to find useful modules and understand the code that was being recommended by stack overflow users. Read about transformation matrices.
* 4pm-5pm: Compiled information in notes and tried to troubleshoot Git issue. It seems as if a file is stuck in the limbo of being committed even though it is no longer tracked and there are commands to remove the file also committed. Ultimately, Git is rejecting all push commands because a .las file exceeding 200mb is present in the files being pushed to Github.
