define([
    'knockout',
    'jquery',
    'arches',
    'viewmodels/workflow',
    'viewmodels/workflow-step'
], function(ko, $, arches, Workflow) {
    return ko.components.register('management-workflow', {
        viewModel: function(params) {

            var self = this;

            params.steps = [
                {
                    title: 'Management Activity Name',
                    name: 'setname',
                    description: 'Name this Activity',
                    component: 'views/components/workflows/new-tile-step',
                    componentname: 'new-tile-step',
                    graphid: '6da8cd00-3c8a-11ea-b9b7-027f24e6fd6b',
                    nodegroupid: '6da8cd37-3c8a-11ea-b9b7-027f24e6fd6b',
                    resourceid: null,
                    tileid: null,
                    parenttileid: null,
                    required: true,
                    icon: 'fa-pencil',
                    wastebin: {resourceid: null, description: 'a consulation instance'}
                },
                {
                    title: 'Consultation Statement',
                    name: 'consultationstatement',
                    description: 'Write a scope of work',
                    component: 'views/components/workflows/new-tile-step',
                    componentname: 'new-tile-step',
                    graphid: '6da8cd00-3c8a-11ea-b9b7-027f24e6fd6b',
                    nodegroupid: '5a8422ad-3cac-11ea-b9b7-027f24e6fd6b',
                    resourceid: null,
                    tileid: null,
                    parenttileid: null,
                    required: false,
                    icon: 'fa-pencil-square-o'
                },
                {
                    title: 'Consultation GeoJSON',
                    name: 'consultationlocation',
                    description: 'Set geospatial data for this consultation',
                    component: 'views/components/workflows/new-tile-step',
                    componentname: 'new-tile-step',
                    graphid: '6da8cd00-3c8a-11ea-b9b7-027f24e6fd6b',
                    nodegroupid: '429130d2-6b27-11ea-b9b7-027f24e6fd6b',
                    resourceid: null,
                    tileid: null,
                    parenttileid: null,
                    required: false,
                    icon: 'fa-map-marker'
                },
                {
                    title: 'Direct Impacts',
                    name: 'directimpacts',
                    description: 'Directly Impacted stuff',
                    component: 'views/components/workflows/new-tile-step',
                    componentname: 'new-tile-step',
                    graphid: '6da8cd00-3c8a-11ea-b9b7-027f24e6fd6b',
                    nodegroupid: '344a48d8-f47a-11ea-a92a-a683e74f6c3a',
                    resourceid: null,
                    tileid: null,
                    parenttileid: null,
                    required: true,
                    icon: 'fa-arrow-circle-down',
                    wastebin: {resourceid: null, description: 'a physical thing instance'}
                }, 
                {
                    title: 'Indirect Impacts',
                    name: 'indirectimpacts',
                    description: 'Indirectly Impacted stuff',
                    component: 'views/components/workflows/new-tile-step',
                    componentname: 'new-tile-step',
                    graphid: '6da8cd00-3c8a-11ea-b9b7-027f24e6fd6b',
                    nodegroupid: 'f36b5244-f479-11ea-a92a-a683e74f6c3a',
                    resourceid: null,
                    tileid: null,
                    parenttileid: null,
                    required: true,
                    icon: 'fa-arrow-circle-o-down',
                    wastebin: {resourceid: null, description: 'a physical thing instance'}
                }, 
                {
                    title: 'Consultation Details',
                    name: 'setdetails',
                    description: 'Consultation Details',
                    component: 'views/components/workflows/new-tile-step',
                    componentname: 'new-tile-step',
                    graphid: '6da8cd00-3c8a-11ea-b9b7-027f24e6fd6b',
                    nodegroupid: '6da8cd16-3c8a-11ea-b9b7-027f24e6fd6b',
                    resourceid: null,
                    tileid: null,
                    parenttileid: null,
                    required: true,
                    class: '',
                    icon: 'fa-calendar-o'
                },
                // {
                //     title: 'Consultation Type',
                //     name: 'setconstype',
                //     description: 'Consultation Type',
                //     component: 'views/components/workflows/new-tile-step',
                //     componentname: 'new-tile-step',
                //     graphid: '6da8cd00-3c8a-11ea-b9b7-027f24e6fd6b',
                //     nodegroupid: '502f401e-3cae-11ea-b9b7-027f24e6fd6b',
                //     resourceid: null,
                //     tileid: null,
                //     parenttileid: null,
                //     required: true,
                //     icon: 'fa-list-alt'
                // },
                {
                    title: 'Action Agents',
                    description: 'Identify the key people/organizations associated with this consultation',
                    component: 'views/components/workflows/new-multi-tile-step',
                    componentname: 'new-multi-tile-step',
                    graphid: '6da8cd00-3c8a-11ea-b9b7-027f24e6fd6b',
                    nodegroupid: '6da8cd28-3c8a-11ea-b9b7-027f24e6fd6b',
                    resourceid: null,
                    tileid: null,
                    parenttileid: null,
                    required: false,
                    icon: 'fa-users'
                },
                {
                    title: 'Consultation Status',
                    name: 'setstatus',
                    description: 'Consultation Status',
                    component: 'views/components/workflows/new-tile-step',
                    componentname: 'new-tile-step',
                    graphid: '6da8cd00-3c8a-11ea-b9b7-027f24e6fd6b',
                    nodegroupid: '83f05a05-3c8c-11ea-b9b7-027f24e6fd6b',
                    resourceid: null,
                    tileid: null,
                    parenttileid: null,
                    required: true,
                    class: '',
                    icon: 'fa-calendar-o'
                },
                {
                    title: 'Add Consulation Complete',
                    description: 'Choose an option below',
                    component: 'views/components/workflows/final-step',
                    componentname: 'final-step',
                    graphid: '6da8cd00-3c8a-11ea-b9b7-027f24e6fd6b',
                    nodegroupid: '83f05a05-3c8c-11ea-b9b7-027f24e6fd6b', // consultation status
                    icon: 'fa-check',
                    resourceid: null,
                    tileid: null,
                    parenttileid: null
                }
            ];

            Workflow.apply(this, [params]);
            // this.quitUrl = "/arches-her" + arches.urls.plugin('init-workflow');
            // console.log(this.quitUrl);
            self.getJSON('management-workflow');

            self.activeStep.subscribe(this.updateState);

            self.ready(true);
        },
        template: { require: 'text!templates/views/components/plugins/management-workflow.htm' }
    });
});
