unfortunately# Nick Catanzaro 2021 SSF Activity Log  

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

## 06/21/2021
* 8:45-9:30am: Meeting with Chris, recorded tasks for the next couple days
* 9:30am-10am: Emailed SSF Research and Communication Plan to Kama. Reviewed last weeks notes and planned out work schedule.
* 10am-12pm: Continued annotating "Optical wave gauging using deep neural networks" (Buscombe et al, 2019).
* 12pm-2:30pm: WHOI Software Carpentry Python Workshop
* 3:45pm-5:10pm: Finished annotating "Optical wave gauging using deep neural networks" (Buscombe et al, 2019).

## 06/22/2021
* 12pm-2:30pm: Annotated "Empirical parameterization of setup, swash, and runup" (Stockdon et al., 2006)
* 2:30-3pm: Created Buoy_Statistics .ipynb and began reviewing buoy data.
* 3pm-4pm: Explored .txt files of buoy historical data. Tried to find the source 99.00 values in all Great Lakes datasets. Note: No spectral wave data is collected in Great Lakes.
* 4pm-5pm: Coastcams Summer Lab meeting. Connected Stockdon equation to operational forecasts/models. Still not completely grounded in the physics of the equation and TWL, but I have a much better understanding and supplemented some coastal morphology knowledge I already had.
* 5pm-7pm: Wrote up workflow and code for making a useable pandas dataframe from NCDB .txt files. Note, there are GitHub repos that could do this faster, but I am trying to make it a learning process and produce my own code. Connecting image timestamps will be interesting depending on how the archives are stored/how extensive they are. Even after removing a lot of values because they contained 99.00, the 2020 dataset on the Muskegon buoy still had over 13,000 rows.
* 7pm-8pm: Compiled notes and further questions in NDCB Buoy information page. Scanned through the DuneX proposal (Will need to a deeper dive later, really interesting work is going to be done!). Added files to GitHub. Reviewed TWL jupyter notebook. Read about different probabilty statistics in python.

## 06/23/2021
* 9:10am-10am: Emailed Steve Ruberg about what images I would like on the hard drive he is creating. Looked through the metdata for buoy images and TBI images.
* 10am-11am: Found the nortek version of the wave data on GLERL's website. Data has not gone through as much processing as NDCB product, yet has less errors and would be easier to read potentially. Looked over wget function notes and the buscombe OWG notebook forwarded by Chris Sherwood.
* 11am-12:30pm: SSF Lecture from Tom Hall on Remote Sensing of Giant Kelp forests and his path from social science to STEM. Encouraging to see other people have done what I am doing.
* 1pm-3:35pm: WHOI Software Carpentry workshop
* 4pm-5:15pm: Woodwell Climate Research Center presentation on Indigenous Perspectives in climate science.
* 5:15pm-6:10pm: Used excel to compare GLERL .csv data that did not go through NDCB post-processing with the .txt files from the NDCB.

## 06/24/2021
* 9am-10:20am: Meeting with Chris Sherwood, paths foward for Buoy_Statistics.ipynb and computing power.
* 10:20am-2:30pm: Use python and pandas library to change the date column of a dataframe into a datetime object, remove unwanted data, and plot data using matplotlib.
* 3:00pm-5:10pm: Read through the example code and update my code. Wrote the wavetxt2waveframe function that takes a list of .txt files from the NDCB and creates a single dataframe of all the relevant wave data. (Could be updated to include average period or specral data for other uses. Could be upgraded by using urls to autoamte the compliling of the list of .txt files)
* 5:10pm-5:30pm: Update SSF_Log, wrote out Friday tasks, Tested wavetxt2waveframe function (it works!)

## 06/25/2021
* 9am-: 10amEmailed Thomas Bell at WHOI regarding the code he used to perform spatial unmixing for The Nature Conservancy. Reviewed Google Earth Engine requirements and python API (might be worth learning some javascript later down the line).  Checked open time for PIV card pickup and activation at the USDA station.
* 10am-11am: Looked through Stack Overflow and pandas docs to find different types of statistical analysis.
* 11am-1:30pm: Made lists of standard deviations for each month on the Muskegon webcam. Used a dictionary to write code that called the month of highest wave variability based on the pandas dataframe.var() function.
* 2pm-4pm: Went through geturl Stack Overflow page and looked at webcam urls to record similarities. Updated NDCB buoy notes and wrote mapped out new ways to work with the data.
* 4pm-7pm: SSF meetup on gather.town.

## 06/28/2021
* 9am-9:40am: Meeting with Chris Sherwood and Rich Signell. Discussed access to AWS cloud computing capabilities. Set a plan for code to be done this week while waiting for data and cloud access.
* 10am-11am: Reviewed .ipynb files. Helped with fridge malfunction in Hardisty lab (all samples were saved!).
* 11am-12pm: Updated SSF_Log, reviewed emails, started AWS application, organized upcoming workflow for creating scatterplots, histograms, and running statistical analyses on buoy data using numpy's statistics.
* 1pm-1:30pm: Began working on Buoy_Statistics notebook using numpy arrays.
* 1:30pm-3:00pm: WHOI MATLAB tutorial
* 3:00pm-5:10pm: Created a scatter plot and performed a linear regression on the buoy data (positive correlation). Plotted wave height for each year's October data (very strange results).

## 06/29/2021
* 10am-11:10am: SSF "What happens next?" chat.
* 11:10am-1pm: Went to credentialing office on and picked up my PIV card and activated it. Read about the artificial intelligence, machine learning, and deep learning
* 1pm-4pm: Created the plots for the Buoy_Statistics notebook
* 4pm-5pm: USGS Summer Lab Meeting (Great talks, glad people like Lorde)
* 5pm-6pm: Edited Buoy_Statistics plots, organized notebook, added a histogram for wave period, updated weekly task list.

## 06/30/2021
* 8:15-9:15am: Respond to emails, submitted WHOI Poseidon form,
* 9:15am-10:45am: Tried to place a line of best fit on Buoy_Statistics histograms. Read up on different theoretical distributions.
* 11am-12:30pm: SSF Lecture by Carolyn Tepolt (crabs are surprisingly cool).
* 1:15pm-3:15pm: WHOI MATLAB training
* 3:15pm-4pm: Updated SSF_Log, planned Thursday taskflow, HPC application.

## 07/1/2021
* 9am-9:30am: Meeting with Chris received list of tasks.
* 10am-12pm: Looked through buoy statistics notebook for spelling errors and planned presentation of material. AWS application submission.
* 1pm-2pm: Read materials for the WHOI Ethics workshop.
* 2pm-3:40pm: WHOI ethics workshop
* 4pm-5:30pm: Plotted lines onto histograms (concluded that they did not add to the scientific value of the graphic and so removed them from the notebook). Updated SSF_Log, shared calendar, read through scipy docs.  

## 07/02/2021
* 10am-12pm: Created SSF Presentation slides, identified images and graphs, and practiced presentation. Added mental notes as presenter notes will not be availbale to me.
* 1pm-2pm: Update notes, find patterns in glerl urls.
* 2pm-3pm: Picked up hard drive from Steve and chatted about getting more images/touring lab/
* 3pm-5:30pm: Intermittently looked through images on the hard drive and adjsuted the presentation.

## 07/06/2021
* 9am-10am: Created getimages function notebook and reviewed urllib.request docs.
* 10am-11am: Respond to emails, update SSF_Log, plot bell curves on histogram.
* 11am-12:30pm: USGS Center meeting and presentation by Olivia De Meo: "Carbon Cycling in Chesapeake Bay, Antarctica, and more!"
* 1pm-2pm: Meetin with Tom Bell to discuss spectral unmixing and using Google Earth Engine.
* 2pm-3pm: Looked through imagery across all years for MI City.
* 3pm-4pm: Wrote questions for CoastCam meeting, updated notes based on intial impressions and observations of imagery from the hard drive.
* 4pm-5pm: CoastCam Summer Lab Meeting and major Microsoft Teams malfunctions (I'll get it figured out eventually)

## 07/07/2021
* 9:30am-10am: Emails and slide prep
* 10am-10:45am: SSF Maching Learning Chat
* 10:45am-12:05pm: SSF Lecture from Dr. Neel Aluru "Oceans and Human Health: Understanding the mechanisms of toxicity of chemical stressors in the envrionment"
* 12:05pm-1pm: Presentation practice and review session
* 1pm-2:30pm: Revised presentation and reviewedw imagery/Buscombe et al., 2020 paper
* 3:30pm-6pm: Further presentation fine tuning based on Chris' reccomendations, installed MS Visual Studio 2019 Community, CUDA 11.4, and set up tensorflow-gpu envrionment.

## 07/08/2021
* 9am-9:45am: Meeting with Chris. Plan to run owg_train notebook and write function to get buoy images.
* 10am-11am: Forked OpticalWaveGauging_DNN from Dan's GitHub and began local clone. Rewrote base url formula for webcam images to go straght to an image.
* 11am-1pm: Enabled wsl2 to run on my computer and use the one liner wget command to replace the need for web scaping with the buoyimages notebook.
* 1:55pm-5:20pm: SSF Midsummer Presentations and Post presentation debrief.
* 5:20pm-6pm: Started running notebook (tensorflow is properly installed and the GPU is detected, all there is to do now is run it); printed ML papers sent by Dan.
* 7pm-7:30pm: Ran OWG-train notebook

## 07/09/2020:
* 9am-10am: Routine secretarial work. Caught up on emails and revised notes.
* 10am-12pm: Began annotating and taking notes on "70 years of machine learning in geoscience in review" (Dramsch, 2020).
* 1pm-2pm: Read through 2 EOS articles relevant to machine learning.
* 2pm-3pm: Finished annotations and notes on Dramsch, 2020.
* 3pm-4pm: Looked through config.json file Chris sent and noted the strucutre of the truncated csv example that is needed to train OWGs.
* 4pm-5pm: Began planning code for writing my own csv files

## 07/12/2021
* 7am-9am: Made prepdata.ipynb and tested code that I had planned out Friday through weekend.
* 9am-9:45am: Meeting with Chris. Sent my code so he could work out an interpolation example.
* 10am-11am: Added image adjustment code to the prepdata notebook.
* 11am-12:30pm: Worked code into the prepmicityimgs function.
* 1pm-2pm: Removed errors and ensured that OWG images were saved in the appropriate path.
* 2pm-3pm: SSF correspondence, updated SSF_Log, ran prepmicityimgs function for 2017-2020. Continued lit review.

## 07/13/2021:
* 7:30am-8am: Looked through demo_t_interp.ipynb file. Lingering questions over how it functions but each question has an answer after some thought so I am not overly concerned.
* 8am-8:30am: Emailed Chris re: buoy code and planned how to write a .csv file to feed the OWG.
* 8:30am-9am: Created csv_interpoloation.ipynb, organized files, read through Chris' email.
* 9am-10:30am: Wrote interpolators and seperated data from October 2017. Filled notebook and sent Chris a follow up email.
* 10:30am-12pm: Continued work on csv_interpoloation notebook and attended SSF whathappensnext chat.
* 12:30pm-2:00pm: Meeting with Chris to get notebook code running properly.
* 2pm-3pm: Cleaned and commented code ion csv_interpoloation notebook (made pathnames generic variables ) and began prepping OWG_train notebook for using GLERL data.
* 3pm-4pm: Prepped and ran OWG_train, wall time of 7min 24s on a base of 345 images. Error is significantly higher than example but could be made better by filtering through images to remove dark images and images that are completely blurred out.
* 4pm-5pm: Summer lab meeting. Photogrammety Basics lecture from Meg Palmston (really interesting, wish I had more of a head for math).
* 5pm-5:30pm: Sent research updates to Chris and SSF. Updated SSF_Log. Recorded additions that need to be made to csv_interpoloation notebook tomorrow.

## 07/14/2021:
* 11am-12pm: SSF Lecture
* 1:30pm-3pm: WHOI MATLAB workshops
* 5pm-7pm: Added in darkness filter to the csv_interpoloation notebook, experimented with sharpness function.

## 07/15/2021:
* 8am-9am: Addtions to csv_interpoloation notebook, mainly writing an appropriate header onto the training csv.
* 9am-10am: Meeting with Chris, discussed potential conferences and moving forward with the notebook.
* 10:30am-12:30pm: Began work editing and optimizing functions. Annotated "Machine learning components in deterministic models: hybrid synergy in the age of data" (Goldstein and Coco, 2015)
* 12:30pm-3pm: Edited optimizer functions. Spent significant time trying to write code that would make new version files of prep images before csv_interpoloation filtering so that the same year could be used to try different parameters like new sizes and resolutions.
* 3pm-6:30pm: SSF Midsummer lectures and post-presentation meeting.
* 6:30pm-8pm: Continued work optimizing functions. Read about Ocean Survey work, found AGU Machine learning session and looked at Ocean Sciences 2022 page. Emailed Kama about extra time on the Tioga and updated SSF_Log

## 07/16/2021:
* 9am-9:30am: WHOI Occupancy Forms.
* 9:30am-10:30am: Edited OWG notebooks and set image specification for the second trial.
* 10:30am-11am: Looked through AGU and Ocean Science conference information.
* 11am-12pm: Optimized and reorganized functions in prep_images.ipynb by adding additional inputs that give the user more control. Further inputs to automate webcam view separation will become necessary when Muskegon imagery becomes available.
* 1pm-2pm: Reviewed midsummer presentation slides and added reuslts from Trial1 to the slides.
* 2pm-3pm: Worked on Trial1 metdata and updating notes. Looked through Dan's OpticalWaveGauging_DNN repo to better understand the code.
* 3pm-5pm: Hardisty Lab Meeting Slides. Presented and discussed my research with people in the lab. Note: Always good to field questions from friendly people as it helps identify gaps in my own knowledge.
* 7pm-8pm: Ran Trail2 and recorded metadata.
Note: There were more work-related activities on this day, unfortunately planning and recording was interrupted by travel to Huron National Forest.

## 07/20/2021:
* 9am-10am: Corresponded with Steve Ruberg about getting Muskegon imagery onto hard drive. Reviewed emails and week ahead.
* 10am-11am: Met with Steve and updated him on my Trial1 and Trial2 results. Copied images from hard drive and gave him the drive with the expectation of picking it up again with Muskegon imagery.
* 11am-12pm: SSF whathappensnext chat
* 1pm-2pm: Began work on first draft of AGU abstract, put OWG Trial2 figures into a slide for the SummerLab meeting.
* 2pm-3pm: Finished first draft. Began looking for web resources and wikis about deep convolutional neural networks.
* 3pm-4pm: SSF chat, Sent out AGU first draft after another revision,
* 4pm-5pm: Summer Lab meeting, must look into wave data and dig into the thesis that Meg Palmston shared. Must review repo Christie H shared with me
* 6pm-7pm: Wrap up work and emails. Reviewed suggested abstract edits.

## 07/21/2021:
* 9am-10am: Reviewed emails and suggested edits of AGU abstract. Ran wget command to download Muskegon buoy images
* 10am-11am: Reviewed Dan's OpticalWaveGauging_DNN notebook and util.py file functions.
* 11am-12pm: SSF lecture
* 1pm-2pm: Updated SSF_Log, Looked through links in the whathappensnext chat, accepted suggested revisions and began filling in blanks with buoy information. Sent an email to check in with Chris about abstract progress.
* 2pm-3pm: Ran prep_images code on copied images to match what was on the hard drive. Continued revising abstract and began applying model to new images.
* 3pm-6:45pm: Ran the model on all images from 2019, just the images from Sept. and Oct. 2019 and the images from Sept. and Oct. 2017. 2017 images had accurate predictions whereas 2019 images did not. This leads me to believe the model may not be accurate year to year due to changes of the camera angle. Images including the horizon and excluding the horizon were used in the case of 2019 to see if that had a significant impact on reducing or improving the accuracy of predictions, it did not.  

## 07/22/2021:
* 8:30am-9am: Prepared to discuss the lack of accuracy in model estimates with Chris by arranging necessary scatterplots to illustrate the issue. Updated notes and thought of potential reasons and solutions for and to the problem. Reviewed slack event reminders and updated calendar.
* 9am-10am: Meeting with Chris, got plan to continue with abstract and training investigations
* 10am-11am: Discussed WHOI visit with Hardisty lab members. Optimized and moves code from csv_interpolation notebook into functions. Spent time reviewing crs code and also stack exchange code to find r value, scipy or skitlearn are best bets for fitting data and getting an r^2 error metric for abstract.
* 11am-12pm: Ran functions. Must remember to add functions into my SSF_funcs.py file. Removed 30% of data as validation.
* 12pm-1:40pm: REU Geosciences career panel. Aaron Pina (program scientist from NASA) (tilde over n) has offered to chat about opportunities and Ted Bigford (former NOAA habitat manager and MSU alumn) asked me to reach out to him. Do by end of the day.
* 2pm-3:40pm: SSF Poster workshops
* 3:40pm-4:10pm: Trained model using the mcyv22017(validationtrain).csv dataset. Saved weights as a different name, must remember to do this for all following trainings.  Note, do not need to change owgtrainimgs because the config commands will only find images with valid filenames in the appropriate csv's.
* 4:10pm-5:45pm: Used the new model to get error metrics for estimates from 2019 and the independent 2017 data. Revised abstract and sent to Chris. I should revise my code to not create a seperate owg folder. Since the config file only uses images listed in the csv, if I put the quality controls in the prepimages function and only did interpolation in the function where quality control currently occurs, I could streamline the process and not have to have so many copies of images on my computer/tons of confusing files in my directory.
* 5:45pm-6:30pm: Updated SSF_Log. Note, get GitHub repo up to date with local files immediately tomorrow morning. Sent emails to career panelists who indicated that they would speake further with me. Must get more information from Chris about how he had such a cool grad school experience.

## 07/22/2021:
* 8:45am-9:35am: Created third draft of AGU abstract, revised and incorporated Chris' comments, shortened links and edited to get under 2,000 characters (no spaces and not including the header). Sent draft to co-authors
* 9:35am-10am: Followed up with Dan and asked about CNN pooling. Looked at AGU information. Reviewed planner. Planned times for meetings with Aaron Pina (NASA) and Ted Bigford (Former NOAA, now retired w/Coastal Society)
* 10am-10:30am: WHOI Trip logistics
* 10:30am-11am: Setting up meetings within WHOI SSF channels for next week.
* 11am-12pm: Updated calendar and notes.
* 12:30pm-5:10pm: Moved QC to prepowgimages function and added automated view folder separation. Simplified folder creation and directory workflow as apart of csv_interpolation functions. General function automation and optimization. Why are nighttime images/low quality images still able to sneak their way into the dataset?

## 07/26/2021:
* 8:40am-9am: Checked emails, updated calendar, figured out that the QC bug from last week was caused by appending to a list within a for loop and then using said list to calculate a metric that each image had to meet. This resulted in the metric changing as the loop ran allowing some night images that were taken with bright lights to get past the darkness and sharpness quality controls.
* 9am-10am: Meeting with Chris. Got to do list for the week and also talked about grad school. On top of everything else that Chris has done, he has also sailed around the Atlantic Ocean in a 72 foot wooden schooner built in 1932 for the DuPont family to compete in the Bermuda Race. Wow.
* 10am-11:30am: Tested QC code fix.
* 11:30am-12:40pm : WHOI SSF visit details meeting
* 1:40pm-5:22pm: Reviewed buoy imagery, emailed Aaron Pina, reviewed WHOI Packing List, optimized functions (coding was slow today)
* 5:22pm-6pm: Implemented MAPE to estimated folder. R2 score was .68 yet MAPE was 40%. Tomorrow I will use my higher resolution imagery with more stringent QC to train a new model and then see if I can reduce MAPE. 
