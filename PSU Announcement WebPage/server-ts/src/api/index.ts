import Router from 'koa-router'
import announcement from './announcement'
import user_result from './user_result'
import { authMiddleware } from '../auth'

const router = new Router()

router
  .get('/api/greet', async (ctx, next) => {
  ctx.body = {msg: 'Hello world.'}
  })
  
  .use('/api/announcement', authMiddleware, announcement.routes())
  .use('/api/userResult', authMiddleware, user_result.routes())

export default router