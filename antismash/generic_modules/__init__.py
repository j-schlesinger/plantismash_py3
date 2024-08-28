from antismash.generic_modules import (
    fullhmmer,
    #        fullhmmer_dblookup,
    genefinding,
    hmm_detection,
    clusterblast,
    subclusterblast,
    knownclusterblast,
    smcogs,
    coexpress,
    gff_parser,
)


def check_prereqs(options):
    failure_msgs = []
    doptions = vars(options)

    if doptions.get("full_hmmer", False) or doptions.get("inclusive", False):
        failure_msgs.extend(fullhmmer.check_prereqs(options))

    failure_msgs.extend(genefinding.check_prereqs(options))
    failure_msgs.extend(hmm_detection.check_prereqs())

    if doptions.get("smcogs", False):
        failure_msgs.extend(smcogs.check_prereqs(options))

    if doptions.get("clusterblast", False):
        failure_msgs.extend(clusterblast.check_prereqs(options))

    if doptions.get("subclusterblast", False):
        failure_msgs.extend(subclusterblast.check_prereqs(options))

    if doptions.get("knownclusterblast", False):
        failure_msgs.extend(knownclusterblast.check_prereqs(options))

    if doptions.get("coexpress", False):
        failure_msgs.extend(coexpress.check_prereqs(options))

    return failure_msgs
