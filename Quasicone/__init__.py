
# declare global parameter n


def __init__(**kwargs):
    # update parameters:
    import json
    JSON = json.JSONEncoder().encode

    with open("parameters.json", "rw+") as f:
        try: parameters = json.load(f)
        except ValueError,err:
            parameters = {}
            print "Warning: in file parameters.json: ", err ,'\n', f.read()
        # clear file content
        f.seek(0)
        f.truncate()
        # update parameters
        for k, v in kwargs.items():
            parameters[k] = v
        f.write(JSON(parameters))
        f.close()

    import Strategy, Weyl_normal
    from Iterator import iterator
    from Apply_strategy import  Apply_strategy #, Defect
    from Weyl_normal import Weyl_normal_form
