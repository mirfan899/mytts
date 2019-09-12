import re
from subprocess import Popen, PIPE

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from jyutping.jyutping import get_jyutping
from synthesizer.models import Transcript
from .forms import TranscriptForm


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class TranscriptView(View):
    form = TranscriptForm
    template_name = "transcript.html"

    def get(self, request):
        form = self.form(request.POST)
        return render(self.request, self.template_name, {"form": form})

    def post(self, *args, **kwargs):
        pk = "/media/wav/cn.wav"
        if self.request.method == "POST" and self.request.is_ajax():
            form = self.form(self.request.POST)
            if form.is_valid():
                transcript = form.cleaned_data['transcript']
                transcript = re.sub("[，。, . ]+", "", transcript)
                jyutping = " ".join(get_jyutping(transcript))

                model = Transcript(transcript=transcript, jyutping=jyutping)
                model.save()
                pk = str(model.id)
                # subprocess.call(['./ossian.sh', str(pk), jyutping], shell=True)
                process = Popen(['sudo', './ossian.sh', pk, jyutping], stdin=PIPE, stdout=PIPE,
                                stderr=PIPE, shell=False)
                # output = process.communicate()[0]
                output = process.wait()
                pk = pk + ".wav"
            return JsonResponse({"success": True, "path": str("/media/wav/{}".format(pk))}, status=200)
        return JsonResponse({"success": False}, status=400)


def get_transcript(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TranscriptForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a index URL:
            data = form.cleaned_data['transcript']
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TranscriptForm()

    return render(request, 'transcript.html', {'form': form})
