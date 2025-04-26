<!-- source: https://ui.nuxt.com/components/drawer --> # Drawer

[Drawer](https://github.com/unovue/vaul-
vue)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Drawer.vue)

A drawer that smoothly slides in & out of the screen.

## Usage

Use a [Button](/components/button) or any other component in the default slot
of the Drawer.

Then, use the `#content` slot to add the content displayed when the Drawer is
open.

    
    
    <template>
      <UDrawer>
        <UButton label="Open" color="neutral" variant="subtle" trailing-icon="i-lucide-chevron-up" />
    
        <template #content>
          <Placeholder class="h-48 m-4" />
        </template>
      </UDrawer>
    </template>
    

You can also use the `#header`, `#body` and `#footer` slots to customize the
Drawer's content.

### Title

Use the `title` prop to set the title of the Drawer's header.

title

    
    
    <template>
      <UDrawer title="Drawer with title">
        <UButton label="Open" color="neutral" variant="subtle" trailing-icon="i-lucide-chevron-up" />
    
        <template #body>
          <Placeholder class="h-48" />
        </template>
      </UDrawer>
    </template>
    

### Description

Use the `description` prop to set the description of the Drawer's header.

description

    
    
    <template>
      <UDrawer
        title="Drawer with description"
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
      >
        <UButton label="Open" color="neutral" variant="subtle" trailing-icon="i-lucide-chevron-up" />
    
        <template #body>
          <Placeholder class="h-48" />
        </template>
      </UDrawer>
    </template>
    

### Direction

Use the `direction` prop to control the direction of the Drawer. Defaults to
`bottom`.

direction

right

    
    
    <template>
      <UDrawer direction="right">
        <UButton label="Open" color="neutral" variant="subtle" trailing-icon="i-lucide-chevron-up" />
    
        <template #content>
          <Placeholder class="min-w-96 min-h-96 size-full m-4" />
        </template>
      </UDrawer>
    </template>
    

### Inset

Use the `inset` prop to inset the Drawer from the edges.

direction

right

inset

true

    
    
    <template>
      <UDrawer direction="right" inset>
        <UButton label="Open" color="neutral" variant="subtle" trailing-icon="i-lucide-chevron-up" />
    
        <template #content>
          <Placeholder class="min-w-96 min-h-96 size-full m-4" />
        </template>
      </UDrawer>
    </template>
    

### Handle

Use the `handle` prop to control whether the Drawer has a handle or not.
Defaults to `true`.

handle

false

    
    
    <template>
      <UDrawer :handle="false">
        <UButton label="Open" color="neutral" variant="subtle" trailing-icon="i-lucide-chevron-up" />
    
        <template #content>
          <Placeholder class="h-48 m-4" />
        </template>
      </UDrawer>
    </template>
    

### Handle Only

Use the `handle-only` prop to only allow the Drawer to be dragged by the
handle.

handleOnly

true

    
    
    <template>
      <UDrawer handle-only>
        <UButton label="Open" color="neutral" variant="subtle" trailing-icon="i-lucide-chevron-up" />
    
        <template #content>
          <Placeholder class="h-48 m-4" />
        </template>
      </UDrawer>
    </template>
    

### Overlay

Use the `overlay` prop to control whether the Drawer has an overlay or not.
Defaults to `true`.

overlay

false

    
    
    <template>
      <UDrawer :overlay="false">
        <UButton label="Open" color="neutral" variant="subtle" trailing-icon="i-lucide-chevron-up" />
    
        <template #content>
          <Placeholder class="h-48 m-4" />
        </template>
      </UDrawer>
    </template>
    

### Scale background

Use the `should-scale-background` prop to scale the background when the Drawer
is open, creating a visual depth effect. You can set the `set-background-
color-on-scale` prop to `false` to prevent changing the background color.

shouldScaleBackground

true

setBackgroundColorOnScale

true

    
    
    <template>
      <UDrawer should-scale-background set-background-color-on-scale>
        <UButton label="Open" color="neutral" variant="subtle" trailing-icon="i-lucide-chevron-up" />
    
        <template #content>
          <Placeholder class="h-48 m-4" />
        </template>
      </UDrawer>
    </template>
    

Make sure to add the `data-vaul-drawer-wrapper` directive to a parent element
of your app to make this work.

app.vue

    
    
    <template>
      <UApp>
        <div class="bg-default" data-vaul-drawer-wrapper>
          <NuxtLayout>
            <NuxtPage />
          </NuxtLayout>
        </div>
      </UApp>
    </template>
    

nuxt.config.ts

    
    
    export default defineNuxtConfig({
      app: {
        rootAttrs: {
          'data-vaul-drawer-wrapper': '',
          'class': 'bg-default'
        }
      }
    })
    

## Examples

### Control open state

You can control the open state by using the `default-open` prop or the
`v-model:open` directive.

Open

    
    
    <script setup lang="ts">
    const open = ref(false)
    
    defineShortcuts({
      o: () => (open.value = !open.value)
    })
    </script>
    
    <template>
      <UDrawer v-model:open="open">
        <UButton label="Open" color="neutral" variant="subtle" trailing-icon="i-lucide-chevron-up" />
    
        <template #content>
          <Placeholder class="h-48 m-4" />
        </template>
      </UDrawer>
    </template>
    

In this example, leveraging [`defineShortcuts`](/composables/define-
shortcuts), you can toggle the Drawer by pressing `O`.

This allows you to move the trigger outside of the Drawer or remove it
entirely.

### Prevent closing

Set the `dismissible` prop to `false` to prevent the Drawer from being closed
when clicking outside of it or pressing escape.

Open

    
    
    <script setup lang="ts">
    const open = ref(false)
    </script>
    
    <template>
      <UDrawer
        v-model:open="open"
        :dismissible="false"
        :ui="{ header: 'flex items-center justify-between' }"
      >
        <UButton label="Open" color="neutral" variant="subtle" trailing-icon="i-lucide-chevron-up" />
    
        <template #header>
          <h2 class="text-highlighted font-semibold">Drawer non-dismissible</h2>
    
          <UButton color="neutral" variant="ghost" icon="i-lucide-x" @click="open = false" />
        </template>
    
        <template #body>
          <Placeholder class="h-48" />
        </template>
      </UDrawer>
    </template>
    

In this example, the `header` slot is used to add a close button which is not
done by default.

### Responsive drawer

You can render a [Modal](/components/modal) component on desktop and a Drawer
on mobile for example.

Edit profile

    
    
    <script lang="ts" setup>
    import { createReusableTemplate, useMediaQuery } from '@vueuse/core'
    
    const [DefineFormTemplate, ReuseFormTemplate] = createReusableTemplate()
    const isDesktop = useMediaQuery('(min-width: 768px)')
    
    const open = ref(false)
    
    const state = reactive({
      email: undefined
    })
    
    const title = 'Edit profile'
    const description = "Make changes to your profile here. Click save when you're done."
    </script>
    
    <template>
      <DefineFormTemplate>
        <UForm :state="state" class="space-y-4">
          <UFormField label="Email" name="email" required>
            <UInput v-model="state.email" placeholder="[[email protected]](/cdn-cgi/l/email-protection)" required />
          </UFormField>
    
          <UButton label="Save changes" type="submit" />
        </UForm>
      </DefineFormTemplate>
    
      <UModal v-if="isDesktop" v-model:open="open" :title="title" :description="description">
        <UButton label="Edit profile" color="neutral" variant="outline" />
    
        <template #body>
          <ReuseFormTemplate />
        </template>
      </UModal>
    
      <UDrawer v-else v-model:open="open" :title="title" :description="description">
        <UButton label="Edit profile" color="neutral" variant="outline" />
    
        <template #body>
          <ReuseFormTemplate />
        </template>
      </UDrawer>
    </template>
    

### With footer slot

Use the `#footer` slot to add content after the Drawer's body.

Open

    
    
    <script setup lang="ts">
    const open = ref(false)
    </script>
    
    <template>
      <UDrawer
        v-model:open="open"
        title="Drawer with footer"
        description="This is useful when you want a form in a Drawer."
        :ui="{ container: 'max-w-xl mx-auto' }"
      >
        <UButton label="Open" color="neutral" variant="subtle" trailing-icon="i-lucide-chevron-up" />
    
        <template #body>
          <Placeholder class="h-48" />
        </template>
    
        <template #footer>
          <UButton label="Submit" color="neutral" class="justify-center" />
          <UButton
            label="Cancel"
            color="neutral"
            variant="outline"
            class="justify-center"
            @click="open = false"
          />
        </template>
      </UDrawer>
    </template>
    

Expand code

### With command palette

You can use a [CommandPalette](/components/command-palette) component inside
the Drawer's content.

Search users...

    
    
    <script setup lang="ts">
    const searchTerm = ref('')
    
    const { data: users, status } = await useFetch('https://jsonplaceholder.typicode.com/users', {
      key: 'command-palette-users',
      params: { q: searchTerm },
      transform: (data: { id: number, name: string, email: string }[]) => {
        return data?.map(user => ({ id: user.id, label: user.name, suffix: user.email, avatar: { src: `https://i.pravatar.cc/120?img=${user.id}` } })) || []
      },
      lazy: true
    })
    
    const groups = computed(() => [{
      id: 'users',
      label: searchTerm.value ? `Users matching “${searchTerm.value}”...` : 'Users',
      items: users.value || [],
      ignoreFilter: true
    }])
    </script>
    
    <template>
      <UDrawer :handle="false">
        <UButton
          label="Search users..."
          color="neutral"
          variant="subtle"
          icon="i-lucide-search"
        />
    
        <template #content>
          <UCommandPalette
            v-model:search-term="searchTerm"
            :loading="status === 'pending'"
            :groups="groups"
            placeholder="Search users..."
            class="h-80"
          />
        </template>
      </UDrawer>
    </template>
    

Expand code

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`title`| | ` string`  
`description`| | ` string`  
`inset`| `false`| `boolean`Whether to inset the drawer from the edges.  
`content`| | ` DialogContentProps & Partial<EmitsToProps<DialogContentImplEmits>>`The content of the drawer.Show properties

  * `disableOutsidePointerEvents?: boolean`When `true`, hover/focus/click interactions will be disabled on elements outside the `DismissableLayer`. Users will need to click twice on outside elements to interact with them: once to close the `DismissableLayer`, and again to trigger the element.
  * `trapFocus?: boolean`When `true`, focus cannot escape the `Content` via keyboard, pointer, or a programmatic focus. Defaults to `false`.
  * `onEscapeKeyDown?: ((event: KeyboardEvent) => void)`
  * `onPointerDownOutside?: ((event: PointerDownOutsideEvent) => void)`
  * `onFocusOutside?: ((event: FocusOutsideEvent) => void)`
  * `onInteractOutside?: ((event: PointerDownOutsideEvent | FocusOutsideEvent) => void)`
  * `onOpenAutoFocus?: ((event: Event) => void)`
  * `onCloseAutoFocus?: ((event: Event) => void)`

  
`overlay`| `true`| `boolean`Render an overlay behind the drawer.  
`handle`| `true`| `boolean`Render a handle on the drawer.  
`portal`| `true`| ` string | false | true | HTMLElement`Render the drawer in a portal.  
`fixed`| | `boolean`When `true`, don't move the drawer upwards if there's space, but rather only change it's height so it's fully scrollable when the keyboard is open  
`open`| | `boolean`  
`defaultOpen`| | `boolean`Opened by default, skips initial enter animation. Still reacts to `open` state changes  
`activeSnapPoint`| | ` null | string | number`  
`closeThreshold`| | ` number`Number between 0 and 1 that determines when the drawer should be closed. Example: threshold of 0.5 would close the drawer if the user swiped for 50% of the height of the drawer or more.  
`shouldScaleBackground`| | `boolean`  
`setBackgroundColorOnScale`| | `boolean`When `false` we don't change body's background color when the drawer is open.  
`scrollLockTimeout`| | ` number`Duration for which the drawer is not draggable after scrolling content inside of the drawer.  
`dismissible`| `true`| `boolean`When `false` dragging, clicking outside,
pressing esc, etc. will not close the drawer. Use this in combination with the
`open` prop, otherwise you won't be able to open/close the drawer.  
`modal`| `true`| `boolean`When `false` it allows to interact with elements
outside of the drawer without closing it.  
`nested`| | `boolean`  
`direction`| `'bottom'`| ` "top" | "right" | "bottom" | "left"`Direction of the drawer. Can be `top` or `bottom`, `left`, `right`.  
`noBodyStyles`| | `boolean`When `true` the `body` doesn't get any styles assigned from Vaul  
`handleOnly`| | `boolean`When `true` only allows the drawer to be dragged by the `<Drawer.Handle />` component.  
`preventScrollRestoration`| | `boolean`  
`snapPoints`| | ` (string | number)[]`Array of numbers from 0 to 100 that corresponds to % of the screen a given snap point should take up. Should go from least visible. Example `[0.2, 0.5, 0.8]`. You can also use px values, which doesn't take screen height into account.  
`ui`| | ` { overlay?: ClassNameValue; content?: ClassNameValue; handle?: ClassNameValue; container?: ClassNameValue; header?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
`content`| `{}`  
`header`| `{}`  
`title`| `{}`  
`description`| `{}`  
`body`| `{}`  
`footer`| `{}`  
  
### Emits

Event |  Type   
---|---  
`close`| `[]`  
`drag`| `[percentageDragged: number]`  
`release`| `[open: boolean]`  
`update:open`| `[open: boolean]`  
`update:activeSnapPoint`| `[val: string | number]`  
`animationEnd`| `[open: boolean]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        drawer: {
          slots: {
            overlay: 'fixed inset-0 bg-elevated/75',
            content: 'fixed bg-default ring ring-default flex focus:outline-none',
            handle: [
              'shrink-0 !bg-accented',
              'transition-opacity'
            ],
            container: 'w-full flex flex-col gap-4 p-4 overflow-y-auto',
            header: '',
            title: 'text-highlighted font-semibold',
            description: 'mt-1 text-muted text-sm',
            body: 'flex-1',
            footer: 'flex flex-col gap-1.5'
          },
          variants: {
            direction: {
              top: {
                content: 'mb-24 flex-col-reverse',
                handle: 'mb-4'
              },
              right: {
                content: 'flex-row',
                handle: '!ml-4'
              },
              bottom: {
                content: 'mt-24 flex-col',
                handle: 'mt-4'
              },
              left: {
                content: 'flex-row-reverse',
                handle: '!mr-4'
              }
            },
            inset: {
              true: {
                content: 'rounded-lg after:hidden'
              }
            }
          },
          compoundVariants: [
            {
              direction: [
                'top',
                'bottom'
              ],
              class: {
                content: 'h-auto max-h-[96%]',
                handle: '!w-12 !h-1.5 mx-auto'
              }
            },
            {
              direction: [
                'right',
                'left'
              ],
              class: {
                content: 'w-auto max-w-[calc(100%-2rem)]',
                handle: '!h-12 !w-1.5 mt-auto mb-auto'
              }
            },
            {
              direction: 'top',
              inset: true,
              class: {
                content: 'inset-x-4 top-4'
              }
            },
            {
              direction: 'top',
              inset: false,
              class: {
                content: 'inset-x-0 top-0 rounded-b-lg'
              }
            },
            {
              direction: 'bottom',
              inset: true,
              class: {
                content: 'inset-x-4 bottom-4'
              }
            },
            {
              direction: 'bottom',
              inset: false,
              class: {
                content: 'inset-x-0 bottom-0 rounded-t-lg'
              }
            },
            {
              direction: 'left',
              inset: true,
              class: {
                content: 'inset-y-4 left-4'
              }
            },
            {
              direction: 'left',
              inset: false,
              class: {
                content: 'inset-y-0 left-0 rounded-r-lg'
              }
            },
            {
              direction: 'right',
              inset: true,
              class: {
                content: 'inset-y-4 right-4'
              }
            },
            {
              direction: 'right',
              inset: false,
              class: {
                content: 'inset-y-0 right-0 rounded-l-lg'
              }
            }
          ]
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
            drawer: {
              slots: {
                overlay: 'fixed inset-0 bg-elevated/75',
                content: 'fixed bg-default ring ring-default flex focus:outline-none',
                handle: [
                  'shrink-0 !bg-accented',
                  'transition-opacity'
                ],
                container: 'w-full flex flex-col gap-4 p-4 overflow-y-auto',
                header: '',
                title: 'text-highlighted font-semibold',
                description: 'mt-1 text-muted text-sm',
                body: 'flex-1',
                footer: 'flex flex-col gap-1.5'
              },
              variants: {
                direction: {
                  top: {
                    content: 'mb-24 flex-col-reverse',
                    handle: 'mb-4'
                  },
                  right: {
                    content: 'flex-row',
                    handle: '!ml-4'
                  },
                  bottom: {
                    content: 'mt-24 flex-col',
                    handle: 'mt-4'
                  },
                  left: {
                    content: 'flex-row-reverse',
                    handle: '!mr-4'
                  }
                },
                inset: {
                  true: {
                    content: 'rounded-lg after:hidden'
                  }
                }
              },
              compoundVariants: [
                {
                  direction: [
                    'top',
                    'bottom'
                  ],
                  class: {
                    content: 'h-auto max-h-[96%]',
                    handle: '!w-12 !h-1.5 mx-auto'
                  }
                },
                {
                  direction: [
                    'right',
                    'left'
                  ],
                  class: {
                    content: 'w-auto max-w-[calc(100%-2rem)]',
                    handle: '!h-12 !w-1.5 mt-auto mb-auto'
                  }
                },
                {
                  direction: 'top',
                  inset: true,
                  class: {
                    content: 'inset-x-4 top-4'
                  }
                },
                {
                  direction: 'top',
                  inset: false,
                  class: {
                    content: 'inset-x-0 top-0 rounded-b-lg'
                  }
                },
                {
                  direction: 'bottom',
                  inset: true,
                  class: {
                    content: 'inset-x-4 bottom-4'
                  }
                },
                {
                  direction: 'bottom',
                  inset: false,
                  class: {
                    content: 'inset-x-0 bottom-0 rounded-t-lg'
                  }
                },
                {
                  direction: 'left',
                  inset: true,
                  class: {
                    content: 'inset-y-4 left-4'
                  }
                },
                {
                  direction: 'left',
                  inset: false,
                  class: {
                    content: 'inset-y-0 left-0 rounded-r-lg'
                  }
                },
                {
                  direction: 'right',
                  inset: true,
                  class: {
                    content: 'inset-y-4 right-4'
                  }
                },
                {
                  direction: 'right',
                  inset: false,
                  class: {
                    content: 'inset-y-0 right-0 rounded-l-lg'
                  }
                }
              ]
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
            drawer: {
              slots: {
                overlay: 'fixed inset-0 bg-elevated/75',
                content: 'fixed bg-default ring ring-default flex focus:outline-none',
                handle: [
                  'shrink-0 !bg-accented',
                  'transition-opacity'
                ],
                container: 'w-full flex flex-col gap-4 p-4 overflow-y-auto',
                header: '',
                title: 'text-highlighted font-semibold',
                description: 'mt-1 text-muted text-sm',
                body: 'flex-1',
                footer: 'flex flex-col gap-1.5'
              },
              variants: {
                direction: {
                  top: {
                    content: 'mb-24 flex-col-reverse',
                    handle: 'mb-4'
                  },
                  right: {
                    content: 'flex-row',
                    handle: '!ml-4'
                  },
                  bottom: {
                    content: 'mt-24 flex-col',
                    handle: 'mt-4'
                  },
                  left: {
                    content: 'flex-row-reverse',
                    handle: '!mr-4'
                  }
                },
                inset: {
                  true: {
                    content: 'rounded-lg after:hidden'
                  }
                }
              },
              compoundVariants: [
                {
                  direction: [
                    'top',
                    'bottom'
                  ],
                  class: {
                    content: 'h-auto max-h-[96%]',
                    handle: '!w-12 !h-1.5 mx-auto'
                  }
                },
                {
                  direction: [
                    'right',
                    'left'
                  ],
                  class: {
                    content: 'w-auto max-w-[calc(100%-2rem)]',
                    handle: '!h-12 !w-1.5 mt-auto mb-auto'
                  }
                },
                {
                  direction: 'top',
                  inset: true,
                  class: {
                    content: 'inset-x-4 top-4'
                  }
                },
                {
                  direction: 'top',
                  inset: false,
                  class: {
                    content: 'inset-x-0 top-0 rounded-b-lg'
                  }
                },
                {
                  direction: 'bottom',
                  inset: true,
                  class: {
                    content: 'inset-x-4 bottom-4'
                  }
                },
                {
                  direction: 'bottom',
                  inset: false,
                  class: {
                    content: 'inset-x-0 bottom-0 rounded-t-lg'
                  }
                },
                {
                  direction: 'left',
                  inset: true,
                  class: {
                    content: 'inset-y-4 left-4'
                  }
                },
                {
                  direction: 'left',
                  inset: false,
                  class: {
                    content: 'inset-y-0 left-0 rounded-r-lg'
                  }
                },
                {
                  direction: 'right',
                  inset: true,
                  class: {
                    content: 'inset-y-4 right-4'
                  }
                },
                {
                  direction: 'right',
                  inset: false,
                  class: {
                    content: 'inset-y-0 right-0 rounded-l-lg'
                  }
                }
              ]
            }
          }
        })
      ]
    })
    

Expand code

[ContextMenuA menu to display actions when right-clicking on an
element.](/components/context-menu)[DropdownMenuA menu to display actions when
clicking on an element.](/components/dropdown-menu)

