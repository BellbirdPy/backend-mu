'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.Menu
 * @description
 * # Menu
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('Menu',['$location', '$rootScope', function ($location) {
    var sections = [
      {
        name: 'Home',
        type: 'link',
        state: 'dashboard'
      },
      {
        name: 'Manejo',
        type: 'toggle',
        pages: [
          {
            name: 'Inventario',
            type: 'link',
            state: 'inventario',
            icon:''
          }, {
            name: 'Compra de Animales',
            state: 'compra',
            type: 'link',
            icon:''
          },
          {
            name: 'Venta de animales',
            state: 'venta',
            type: 'link',
            icon:''
          },
          {
            name: 'Mortandad y Abigeo',
            state: 'mortandad',
            type: 'link',
            icon:''
          }
        ]
      },
      {
        name: 'Sanitación',
        type: 'link',
        state: 'sanitacion'
      },
      {
        name: 'Nutrición',
        type: 'link',
        state: 'nutricion'
      },
      {
        name: 'Genética',
        type: 'link',
        state: 'genetica'
      },
      {
        name: 'Establecimiento',
        type: 'link',
        state: 'establecimiento'
      },
    ];


    var self;

    return self = {
      sections: sections,

      toggleSelectSection: function (section) {
        self.openedSection = (self.openedSection === section ? null : section);
      },
      isSectionSelected: function (section) {
        return self.openedSection === section;
      },

      selectPage: function (section, page) {
        page && page.url && $location.path(page.url);
        self.currentSection = section;
        self.currentPage = page;
      }
    };

    function sortByHumanName(a, b) {
      return (a.humanName < b.humanName) ? -1 :
        (a.humanName > b.humanName) ? 1 : 0;
    }
  }]);