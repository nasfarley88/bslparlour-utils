from vimeo import VimeoClient
import myconf

vimeo_client = VimeoClient(myconf.ACCESS_TOKEN,
                           myconf.CLIENT_ID,
                           myconf.CLIENT_SECRET)

def upload_list_to_vimeo(filename_list):
    """A simple function to upload all files in a list to Vimeo. """

    for i in filename_list:
        vimeo_client.upload(i)

def video_json_for_database(filename,
                            is_source_video=None,
                            is_not_source_video=None,
                            source_video=None):
    """Returns the json to POST to The BSL Parlour for a given filename. """

    print "This funtion is not fully implemented."
    assert (is_source_video == True
            or is_not_source_video == True), ("You must specify whether"
                                              " this video is a either "
                                              "SourceVideo or NotSourceVideo.")
    if is_not_source_video:
        assert source_video != None, ("You must specify a source video "
                                      "file path for a NotSourceVideo.")
        # TODO: Make sure that TBP database is checked for the source video

    assert False, "This function is not written!"

def upload_list_to_database_and_vimeo(filename_list):
    """TODO this function. """
    assert False, "This function is currently not written"
    
