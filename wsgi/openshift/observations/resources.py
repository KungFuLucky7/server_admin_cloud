from import_export import resources
from observations.models import Observation
from import_export.admin import ImportExportModelAdmin

class ObservationResource(resources.ModelResource):

    class Meta:
        model = Observation
        
class ObservationResourceAdmin(ImportExportModelAdmin):
    resource_class = ObservationResource
    fieldsets = [
        (None,               {'fields': ['species']}),
        (None,               {'fields': ['family']}),
        (None,               {'fields': ['common_name']}),
        ('Published Date',   {'fields': ['timestamp']}),
        ('Observation Type', {'fields': ['observation_type']}),  
        ('Lifeform', 	     {'fields': ['lifeform']}),
        ('Phenology', 	     {'fields': ['phenology']}),
        ('Habitat', 	     {'fields': ['habitat']}),
        ('On Serpentine', 	 {'fields': ['onserpentine']}),
        ('Latitude',         {'fields': ['latitude']}),
        ('Longitude',        {'fields': ['longitude']}),
        ('Location',         {'fields': ['location']}),
        #('GPS',              {'fields': ['gps']}),
        ('Number of Plants', {'fields': ['numplants']}),
        ('Image',            {'fields': ['image']}),
        ('Description',      {'fields': ['description'], 'classes': ['grp-collapse grp-open']}),
        ('Revision Notes',   {'fields': ['revision_notes'], 'classes': ['grp-collapse grp-closed']}),
        ('Observer Name', 	 {'fields': ['observername']}),
        ('Device Name', 	 {'fields': ['devicename']}),
        ('Edited by',        {'fields': ['edited_by']}),
        ('Edited on',        {'fields': ['edited_on']}),
        ('Uploaded',         {'fields': ['uploaded']}),
        ('Validated',        {'fields': ['validated']}),
    ]
    readonly_fields=('timestamp', 'edited_by', 'edited_on')
    list_display = ('species', 'validated', 'uploaded', 'edited_by', 'edited_on', 'family', 'common_name', 'location', 'timestamp', 'observername', 'devicename', 'was_published_recently')
    list_filter = ('validated', 'uploaded', 'timestamp', 'edited_on', 'edited_by', 'species', 'family', 'common_name', 'observation_type', 'lifeform', 'phenology', 'habitat', 'onserpentine', 'location', 'observername', 'devicename')
    search_fields = ('species', 'family', 'common_name', 'timestamp', 'location', 'lifeform', 'phenology', 'habitat', 'observername', 'devicename')
    date_hierarchy = 'timestamp'
    ordering = ['species']

    def save_model(self, request, obj, form, change):
        obj.edited_by = request.user
        obj.save()
