import HomePage from '../pages/HomePage'

import homeNav from '../pages/HomePage/homeNav'

import ClassesRoute from './ClassesRoute'

export default {
  path: '/home',
  alias: '/',
  component: HomePage,
  children: [
    {
      path: '',
      name: HomePage.name,
      component: homeNav
    },
    ClassesRoute
  ]
}
