<!-- source: https://ui.nuxt.com/components/link --> # Link

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Link.vue)

A wrapper around  with extra props.

## Usage

The Link component is a wrapper around
[`<NuxtLink>`](https://nuxt.com/docs/api/components/nuxt-link) using the
[`custom`](https://router.vuejs.org/api/interfaces/RouterLinkProps.html#Properties-
custom) prop. It provides a few extra props:

  * `inactive-class` prop to set a class when the link is inactive, `active-class` is used when active.
  * `exact` prop to style with `active-class` when the link is active and the route is exactly the same as the current route.
  * `exact-query` and `exact-hash` props to style with `active-class` when the link is active and the query or hash is exactly the same as the current query or hash. 
    * use `exact-query="partial"` to style with `active-class` when the link is active and the query partially match the current query.

The incentive behind this is to provide the same API as NuxtLink back in Nuxt
2 / Vue 2. You can read more about it in the Vue Router [migration from Vue
2](https://router.vuejs.org/guide/migration/#removal-of-the-exact-prop-in-
router-link) guide.

It is used by the [`Breadcrumb`](/components/breadcrumb),
[`Button`](/components/button), [`ContextMenu`](/components/context-menu),
[`DropdownMenu`](/components/dropdown-menu) and
[`NavigationMenu`](/components/navigation-menu) components.

### Tag

The `Link` components renders an `<a>` tag when a `to` prop is provided,
otherwise it renders a `<button>` tag. You can use the `as` prop to change
fallback tag.

to

as

    
    
    <template>
      <ULink as="button">Link</ULink>
    </template>
    

You can inspect the rendered HTML by changing the `to` prop.

### Style

By default, the link has default active and inactive styles, check out the
#theme section.

to

    
    
    <template>
      <ULink to="/components/link">Link</ULink>
    </template>
    

Try changing the `to` prop to see the active and inactive states.

You can override this behavior by using the `raw` prop and provide your own
styles using `class`, `active-class` and `inactive-class`.

to

activeClass

inactiveClass

    
    
    <template>
      <ULink raw to="/components/link" active-class="font-bold" inactive-class="text-muted">Link</ULink>
    </template>
    

## IntelliSense

If you're using VSCode and wish to get autocompletion for the classes `active-
class` and `inactive-class`, you can add the following settings to your
`.vscode/settings.json`:

.vscode/settings.json

    
    
    {
      "tailwindCSS.classAttributes": [
        "active-class",
        "inactive-class"
      ]
    }
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'button'`| `any`The element or component this component should render
as when not a link.  
`type`| `'button'`| ` "reset" | "submit" | "button"`The type of the button when not a link.  
`disabled`| | `boolean`  
`active`| `undefined`| `boolean`Force the link to be active independent of the
current route.  
`exact`| | `boolean`Will only be active if the current route is an exact match.  
`exactQuery`| | `boolean | "partial"`Allows controlling how the current route query sets the link as active.  
`exactHash`| | `boolean`Will only be active if the current route hash is an exact match.  
`inactiveClass`| `''`| ` string`The class to apply when the link is inactive.  
`raw`| | `boolean`When `true`, only styles from `class`, `activeClass`, and `inactiveClass` will be applied.  
`to`| | ` string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.Show properties

  * `name?: RouteRecordNameGeneric`
  * `params?: RouteParamsRawGeneric`
  * `path?: undefined`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `replace?: boolean`Replace the entry in the history instead of pushing a new entry
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>
  * `path: string`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `replace?: boolean`Replace the entry in the history instead of pushing a new entry
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>

  
`href`| | ` string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`An alias for `to`. If used with `to`, `href` will be ignoredShow properties

  * `name?: RouteRecordNameGeneric`
  * `params?: RouteParamsRawGeneric`
  * `path?: undefined`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `replace?: boolean`Replace the entry in the history instead of pushing a new entry
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>
  * `path: string`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `replace?: boolean`Replace the entry in the history instead of pushing a new entry
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>

  
`external`| | `boolean`Forces the link to be considered as external (true) or internal (false). This is helpful to handle edge-cases  
`target`| | ` null | string & {} | "_blank" | "_parent" | "_self" | "_top"`Where to display the linked URL, as the name for a browsing context.  
`rel`| | ` null | string & {} | "noopener" | "noreferrer" | "nofollow" | "sponsored" | "ugc"`A rel attribute value to apply on the link. Defaults to "noopener noreferrer" for external links.  
`noRel`| | `boolean`If set to true, no rel attribute will be added to the link  
`prefetchedClass`| | ` string`A class to apply to links that have been prefetched.  
`prefetch`| | `boolean`When enabled will prefetch middleware, layouts and payloads of links in the viewport.  
`prefetchOn`| | ` "visibility" | "interaction" | Partial<{ visibility: boolean; interaction: boolean; }>`Allows controlling when to prefetch links. By default, prefetch is triggered only on visibility.  
`noPrefetch`| | `boolean`Escape hatch to disable `prefetch` attribute.  
`replace`| | `boolean`Calls `router.replace` instead of `router.push`.  
`activeClass`| `''`| ` string`Class to apply when the link is active  
`exactActiveClass`| | ` string`Class to apply when the link is exact active  
`ariaCurrentValue`| `'page'`| ` "date" | "time" | "step" | "page" | "location" | "true" | "false"`Value passed to the attribute `aria-current` when the link is exact active.  
`viewTransition`| | `boolean`Pass the returned promise of `router.push()` to `document.startViewTransition()` if supported.  
  
### Slots

Slot |  Type   
---|---  
`default`| `{ active: boolean; }`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        link: {
          base: 'focus-visible:outline-primary',
          variants: {
            active: {
              true: 'text-primary',
              false: [
                'text-muted hover:text-default',
                'transition-colors'
              ]
            },
            disabled: {
              true: 'cursor-not-allowed opacity-75'
            }
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            link: {
              base: 'focus-visible:outline-primary',
              variants: {
                active: {
                  true: 'text-primary',
                  false: [
                    'text-muted hover:text-default',
                    'transition-colors'
                  ]
                },
                disabled: {
                  true: 'cursor-not-allowed opacity-75'
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            link: {
              base: 'focus-visible:outline-primary',
              variants: {
                active: {
                  true: 'text-primary',
                  false: [
                    'text-muted hover:text-default',
                    'transition-colors'
                  ]
                },
                disabled: {
                  true: 'cursor-not-allowed opacity-75'
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[KbdA kbd element to display a keyboard key.](/components/kbd)[ModalA dialog
window that can be used to display a message or request user
input.](/components/modal)

